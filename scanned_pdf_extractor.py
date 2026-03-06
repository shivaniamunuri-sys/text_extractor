from utils.pdf_to_image import pdf_to_images
from extractors.image_ocr_extractor import extract_text_from_image

def extract_text_from_scanned_pdf(pdf_path):
    images = pdf_to_images(pdf_path)
    text = ""
    for image in images:
        text += extract_text_from_image(image)
    return text