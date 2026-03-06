from extractors.pdf_extractor import extract_pdf_text
from extractors.scanned_pdf_extractor import extract_text_from_scanned_pdf

def process_pdf(file_path):
    text = extract_pdf_text(file_path)

    if len(text.strip()) < 10:
        print("Scanned PDF detected. Running OCR...")
        text = extract_text_from_scanned_pdf(file_path)

    return text