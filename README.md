# PDF to Word Converter

This project provides a simple Python script to convert PDF files to Word (.docx) documents using `pdfplumber` and `python-docx`.

## Features
- Extracts text from each page of a PDF file
- Saves the extracted text into a Word document, with each page as a new paragraph

## Requirements
- Python 3.6 or higher
- [pdfplumber](https://pypi.org/project/pdfplumber/)
- [python-docx](https://pypi.org/project/python-docx/)

## Installation
1. Clone or download this repository.
2. Install the required Python packages:
   ```bash
   pip install pdfplumber python-docx
   ```

## Usage
1. Place the PDF file you want to convert in the project directory.
2. Edit `test.py` and set the `pdf_file` and `word_file` variables to your desired input and output file names:
   ```python
   pdf_file = "your_file.pdf"  # Replace with your PDF file name
   word_file = "output.docx"   # Replace with your desired Word file name
   ```
3. Run the script:
   ```bash
   python test.py
   ```
4. The converted Word document will be saved in the project directory.

## Notes
- Only text is extracted; images and complex formatting are not preserved.
- Make sure your PDF file is not encrypted or password-protected.

## Example
If you have a file named `test.pdf`, you can run:
```bash
python test.py
```
This will create a file named `example.docx` with the extracted text.

---

Feel free to modify the script for more advanced PDF-to-Word conversion needs. 