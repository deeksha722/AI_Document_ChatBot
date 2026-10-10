from io import BytesIO
from pypdf import PdfReader


def read_pdf(pdf_bytes):
    """
    Extract text from a PDF file.

    pdf_bytes: The uploaded PDF as bytes.
    """

    reader = PdfReader(BytesIO(pdf_bytes))

    pages_text = []

    for page in reader.pages:
        text = page.extract_text() or ""

        if text.strip():
            pages_text.append(text)

    full_text = "\n".join(pages_text)

    if not full_text.strip():
        raise ValueError(
            "No readable text found in the PDF."
        )

    return full_text