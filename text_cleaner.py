import re

def clean_text(text):

    if not text:
        return ""

    # normalize new lines
    text = text.replace("\r\n", "\n")

    # remove multiple spaces
    text = re.sub(r"[ \t]+", " ", text)

    # remove multiple empty lines
    text = re.sub(r"\n{2,}", "\n", text)

    return text.strip()