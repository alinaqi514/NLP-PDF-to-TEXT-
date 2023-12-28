import PyPDF2

# Open the PDF file in read-binary mode
pdf_file = open('PatientReport.pdf', 'rb')

# Create a PDF file reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF
num_pages = len(pdf_reader.pages)

# Create a new TXT file
with open('PatientReport.txt', 'w', encoding='utf-8') as txt_file:

    # Loop through each page and extract the text
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        txt_file.write(text)

# Close the PDF file
pdf_file.close()
