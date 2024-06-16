import fitz  # PyMuPDF

def extract_core_highlighted_text(pdf_path):
    doc = fitz.open(pdf_path)
    core_highlighted_text = []
    for page in doc:
        annotations = page.annots()
        if annotations:
            for annot in annotations:
                if annot.type[0] == 8:  # Highlight annotation type
                    rect = annot.rect
                    words = page.get_text("words")
                    words_in_rect = [w for w in words if fitz.Rect(w[:4]).intersects(rect)]
                    full_sentence = " ".join(w[4] for w in words_in_rect)
                    
                    # Split the sentence into segments based on full stops
                    sentences = full_sentence.split('.')
                    for sentence in sentences:
                        # Trim leading and trailing whitespace
                        trimmed_sentence = sentence.strip()
                        # Check if the sentence contains significant content from the highlight
                        if any(word in trimmed_sentence for word in [w[4] for w in words_in_rect]):
                            # Further refine here if necessary, e.g., by checking keyword density
                            core_highlighted_text.append(trimmed_sentence)
    return core_highlighted_text

# Use the function
pdf_path = 'data/Aldasoro et al. - Intelligent financial system how AI is transformi.pdf'
highlights = extract_core_highlighted_text(pdf_path)
print("\n".join(highlights))