import re
import fitz  # PyMuPDF

# Regex patterns
EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
PHONE_REGEX = r"\+?\d{1,3}?[-.\s]??(?:\(?\d{2,4}\)?[-.\s]?)*\d{3,4}[-.\s]?\d{3,4}"

def clean_pdf(input_path: str, output_path: str, mode: str = "mask"):
    doc = fitz.open(input_path)

    for page in doc:
        # Tìm và xử lý email
        for match in re.findall(EMAIL_REGEX, page.get_text("text")):
            rects = page.search_for(match)
            for r in rects:
                if mode == "mask":
                    page.add_redact_annot(r, fill=(0, 0, 0))
                else:
                    page.add_redact_annot(r, text="")

        # Tìm và xử lý số điện thoại
        for match in re.findall(PHONE_REGEX, page.get_text("text")):
            rects = page.search_for(match)
            for r in rects:
                if mode == "mask":
                    page.add_redact_annot(r, fill=(0, 0, 0))
                else:
                    page.add_redact_annot(r, text="")

        page.apply_redactions()

    doc.save(output_path)
    doc.close()
