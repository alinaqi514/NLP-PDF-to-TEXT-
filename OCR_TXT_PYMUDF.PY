import pytesseract
from pdf2image import convert_from_path

# Replace 'PatientReport.pdf' with the name of your PDF file
pdf_file = 'PatientReport.pdf'

# Convert PDF to images
pages = convert_from_path(pdf_file, 500)

# Convert images to text using OCR
text = ''
for page in pages:
    text += pytesseract.image_to_string(page)

# Write the text to a TXT file
with open('PatientReport.txt', 'w') as f:
    f.write(text)
