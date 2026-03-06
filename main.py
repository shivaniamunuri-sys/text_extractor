from utils.file_detector import detect_file_type
from processors.pdf_processor import process_pdf
from extractors.docx_extractor import extract_docx_text
from extractors.txt_extractor import extract_txt_text
from processors.image_processor import process_image
from utils.text_cleaner import clean_text
from extractors.two_column_extractor import extract_two_column
print("Import works!")
def extract_resume_text(file_path):

    file_type = detect_file_type(file_path)

    if file_type == "pdf":
        text = process_pdf(file_path)

    elif file_type == "docx":
        text = extract_docx_text(file_path)

    elif file_type == "txt":
        text = extract_txt_text(file_path)

    elif file_type == "image":
        text = process_image(file_path)

    else:
        print("\n Unsupported file format")
        return None

    text = clean_text(text)

    return text


def is_resume(text):

    resume_keywords = [
        "education",
        "experience",
        "skills",
        "projects",
        "internship",
        "summary",
        "contact"
    ]

    text_lower = text.lower()

    for word in resume_keywords:
        if word in text_lower:
            return True

    return False


if __name__ == "__main__":

    file_path = input("Enter resume file path: ").strip().strip('"').strip("'")

    text = extract_resume_text(file_path)

    if text is None:
        exit()

    if not is_resume(text):
        print("\n This file is not a resume")
        exit()

    print("\n Resume detected")

    print("\nExtracted Text:\n")
    print(text)