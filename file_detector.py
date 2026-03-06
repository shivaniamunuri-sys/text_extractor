import os

def detect_file_type(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return "pdf"
    elif ext == ".docx":
        return "docx"
    elif ext == ".txt":
        return "txt"
    elif ext in [".png", ".jpg", ".jpeg"]:
        return "image"

    return "unknown"