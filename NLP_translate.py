from googletrans import Translator
import fitz  # PyMuPDF
from reportlab.pdfgen import canvas

def translate_text(text, source_lang='en', target_lang='ur'):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

def translate_pdf(input_pdf, output_pdf):
    pdf_document = fitz.open(input_pdf)
    pdf_writer = canvas.Canvas(output_pdf)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text = page.get_text()
        translated_text = translate_text(text)
        
        # Adjust the coordinates as needed
        pdf_writer.drawString(10, 800, translated_text)

    pdf_writer.save()

input_pdf_path = 'LabTask7.pdf'
output_pdf_path = 'translate3.pdf'

translate_pdf(input_pdf_path, output_pdf_path)
