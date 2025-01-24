import pdfplumber
from docx import Document


def pdf_to_word(pdf_file, word_file):
    # Open the PDF file
    with pdfplumber.open(pdf_file) as pdf:
        # Create a Word document
        doc = Document()

        # Iterate through the pages in the PDF
        for page in pdf.pages:
            # Extract text from the page
            text = page.extract_text()
            if text:
                # Add the text to the Word document
                doc.add_paragraph(text)

        # Save the Word document
        doc.save(word_file)
        print(f"Successfully converted {pdf_file} to {word_file}")


# Example usage
pdf_file = "test.pdf"  # Replace with your PDF file name
word_file = "example.docx"  # Replace with your desired Word file name

pdf_to_word(pdf_file, word_file)
