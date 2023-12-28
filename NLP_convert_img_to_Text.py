from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image

def convert_pdf_to_img(pdf_file):
    return convert_from_path(pdf_file)

def convert_img_to_text(file):
    text= image_to_string(file)
    return text
def get_text_from_any_pdf(pdf_file):
    images = convert_pdf_to_img(pdf_file)
    text = ''
    for page ,img in enumerate(images):
        text += convert_img_to_text(page)
    return text
path_to_pdf = r"C:\Users\bauss\Desktop\Open CV\PatientReport.pdf"

print (get_text_from_any_pdf(path_to_pdf))