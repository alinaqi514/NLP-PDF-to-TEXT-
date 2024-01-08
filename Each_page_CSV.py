import pytesseract
from pdf2image import convert_from_path
import csv

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

# Define keywords for each column
keywords = {
    'Hospital Name': 'DIAGNOSTIC CENTRE',
    'LAB ID': 'BID',
    'Name': 'Pat. Name',
    'Refer By': 'Refer By',
    'Sample Date': 'Sample Date',
    'Patient ID': 'Patient ID',
    'Age/sex': 'Age / Sex',
    'WBC count': 'BC Count',
    'RBC count': 'RBC Count'
}

# Process each page
for i, page in enumerate(pages):
    try:
        # OCR to extract text
        page_text = pytesseract.image_to_string(page)

        # Extract information using keywords
        data = {}
        for column, keyword in keywords.items():
            if keyword in page_text:
                value = page_text.split(keyword, 1)[1].strip().split('\n')[0]
                data[column] = value

        # Write data to CSV file
        output_csv_file = f'Page_{i + 1}_output.csv'
        with open(output_csv_file, 'w', encoding='utf-8', newline='') as csv_file:
            fieldnames = ['Hospital Name', 'LAB ID', 'Name', 'Refer By', 'Sample Date', 'Patient ID', 'Age/sex', 'WBC count', 'RBC count']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)

        print(f"Page {i + 1} data successfully written to {output_csv_file}")
    except Exception as e:
        print(f"Error processing page {i + 1}: {e}")


