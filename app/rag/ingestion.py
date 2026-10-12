from pathlib import Path

from pypdf import PdfReader

def extract_pdf_pages(pdf_path: str) -> list[dict]:
    path = Path(pdf_path)

    if not path.is_file():
        raise FileNotFoundError(f"PDF not found: {path}")

    reader = PdfReader(str(path))
    extracted_pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text.strip():
            extracted_pages.append(
                {
                    "text": text.strip(),
                    "metadata": {
                        "source": path.name,
                        "page": page_number,
                    },
                }
            )

    return extracted_pages
