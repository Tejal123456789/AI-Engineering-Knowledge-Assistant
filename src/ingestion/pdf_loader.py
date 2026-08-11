from pypdf import PdfReader


def load_pdf(pdf_path):
    """
    Read a PDF and return all text as a single string.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text