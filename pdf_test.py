from pypdf import PdfReader
import os

def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")

    reader = PdfReader(pdf_path)
    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    return full_text

pdf_path = "sreeja_resumeupdate.pdf"   # exact file name with extension
text = extract_text_from_pdf(pdf_path)

print(text[:2000])
