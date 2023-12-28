import PyPDF2
import docx

# Open the PDF file in read-binary mode
pdf_file = open('LabTask7.pdf', 'rb')

# Create a PDF file reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF
num_pages = len(pdf_reader.pages)

# Create a new Word document
doc = docx.Document()

# Loop through each page and extract the text
for page_num in range(num_pages):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    doc.add_paragraph(text)

# Save the Word document
doc.save('LabTask7.docx')

# Close the PDF file
pdf_file.close()