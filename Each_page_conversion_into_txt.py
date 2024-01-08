import pytesseract
from pdf2image import convert_from_path

# Replace 'Samples - 30.pdf' with the name of your PDF file
pdf_file = 'Samples - 30.pdf'

# Specify the path to the Tesseract executable if needed
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Convert PDF to images
try:
    pages = convert_from_path(pdf_file, 500)
except Exception as e:
    print(f"Error converting PDF to images: {e}")
    quit()

# Convert images to text using OCR and write each page to a separate TXT file
for i, page in enumerate(pages):
    try:
        page_text = pytesseract.image_to_string(page)
        output_file = f'Page_{i + 1}.txt'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(page_text)
        print(f"Page {i + 1} text successfully written to {output_file}")
    except Exception as e:
        print(f"Error processing page {i + 1}: {e}")
