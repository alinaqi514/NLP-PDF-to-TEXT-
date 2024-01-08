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

# Convert images to text using OCR
text = ''
for i, page in enumerate(pages):
    try:
        page_text = pytesseract.image_to_string(page)
        print(f"Page {i + 1} Text:\n{page_text}\n{'-' * 30}")
        text += page_text
    except Exception as e:
        print(f"Error processing page {i + 1}: {e}")

# Write the text to a TXT file
output_file = 'S1.txt'
try:
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Text successfully written to {output_file}")
except Exception as e:
    print(f"Error writing text to {output_file}: {e}")
