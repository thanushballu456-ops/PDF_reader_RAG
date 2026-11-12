from pathlib import Path
import re
import unicodedata
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from endee import Endee, Precision

INDEX_NAME = "documents_v2"
PDF_PATH = Path(r"C:\Users\umama\Desktop\endee project\sreeja_resumeupdate.pdf")

def extract_text_from_pdf(pdf_path):
    """Pull raw text out of every page of the PDF."""
    reader = PdfReader(str(pdf_path))
    full_text = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text.append(text)
    return "\n".join(full_text)

def clean_text(text):
    """Fix common PDF extraction issues: ligatures, weird whitespace."""
    text = unicodedata.normalize("NFKD", text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def chunk_text(text, chunk_size=800, overlap=150):
    """Split text into overlapping character-based chunks."""
    chunks = []
    start = 0
    step = max(1, chunk_size - overlap)

    while start < len(text):
        chunk = text[start:start + chunk_size]
        if chunk.strip():
            chunks.append(chunk)
        start += step

    return chunks

def main():
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"PDF not found: {PDF_PATH}")

    client = Endee()

    # Create the index, but don't crash if it already exists from a previous run
    try:
        client.create_index(name=INDEX_NAME, dimension=384, space_type="cosine", precision=Precision.INT8)
        print(f"Index '{INDEX_NAME}' created successfully")
    except Exception as e:
        if "already exists" in str(e).lower():
            print(f"Index '{INDEX_NAME}' already exists, continuing...")
        else:
            raise

    index = client.get_index(name=INDEX_NAME)
    print(f"Index '{INDEX_NAME}' fetched successfully")

    # 1. Extract raw text from the PDF
    text = extract_text_from_pdf(PDF_PATH)
    if not text.strip():
        raise ValueError("No text extracted from PDF")

    # 2. Clean it up (fix ligatures, collapse whitespace)
    text = clean_text(text)

    # 3. Split into overlapping chunks
    chunks = chunk_text(text)
    print("Total chunks:", len(chunks))

    # 4. Embed all chunks
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)

    # 5. Package each chunk + its vector + metadata for upserting
    vectors = []
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings), start=1):
        vectors.append({
            "id": f"resume_chunk_{i}",
            "vector": emb.tolist(),
            "meta": {
                "chunk_number": i,
                "text": chunk
            }
        })

    # 6. Upsert into Endee
    index.upsert(vectors)
    print(f"Upsert successful: {len(vectors)} vectors inserted")

    # 7. Sanity-check query — search using the first chunk's own vector
    results = index.query(vector=embeddings[0].tolist(), top_k=3)
    print("\nQuery results:")
    for item in results:
        print(item)

if __name__ == "__main__":
    main()