from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    return full_text

def chunk_text(text, chunk_size=800, overlap=150):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks

pdf_path = "sreeja_resumeupdate.pdf"
text = extract_text_from_pdf(pdf_path)

chunks = chunk_text(text)

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks[:3]):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk)

    
