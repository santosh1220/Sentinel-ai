from app.rag.ingestion import extract_pdf_pages

pages = extract_pdf_pages("data/security_policy.pdf")

for item in pages:
    print(f"\nSource: {item['metadata']['source']}")
    print(f"Page: {item['metadata']['page']}")
    print(f"Text: {item['text']}")
