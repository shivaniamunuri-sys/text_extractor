import fitz

def extract_two_column(file_path):

    doc = fitz.open(file_path)

    full_text = ""

    for page in doc:

        blocks = page.get_text("blocks")

        page_width = page.rect.width
        middle = page_width / 2

        left_column = []
        right_column = []

        for block in blocks:

            x0, y0, x1, y1, text, *_ = block

            text = text.strip()

            if not text:
                continue

            if x0 < middle:
                left_column.append((y0, text))
            else:
                right_column.append((y0, text))

        # sort top → bottom
        left_column.sort(key=lambda x: x[0])
        right_column.sort(key=lambda x: x[0])

        # merge columns
        for _, t in left_column:
            full_text += t + "\n"

        for _, t in right_column:
            full_text += t + "\n"

    return full_text