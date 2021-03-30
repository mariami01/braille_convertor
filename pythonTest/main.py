from pybraille.main import convertText, convertFile
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
import io

import pyautogui
from PIL import Image
from pytesseract import *  

# converts text to braile and writes in a diff file
def main():
    file1 = open('mytext.txt', 'r')
    file2 = open('convertedText.txt', 'w')

    for i in file1.readlines():
        file2.write(convertText(i))

    file1.close()
    file2.close()

def txt2brl(txt):
    output = ''
    for page in txt:
        output += convertText(page)
    return str(output)

# main()

# coonverts pdf to text and outputs in a diff file
def pdfToText(PDFfile, outTXTfile):
    inFile = open(PDFfile, 'rb')
    resource_manager = PDFResourceManager(caching=True)
    out_text = io.StringIO()
    text_converter = TextConverter(resource_manager, out_text, laparams=LAParams())
    interpreter = PDFPageInterpreter(resource_manager, text_converter)
    # process each page in pdf file
    for page in PDFPage.get_pages(inFile):
        interpreter.process_page(page)

    text = out_text.getvalue()
    out = ''
    for i in text:
        out += txt2brl(i)
    # save output data to a text file
    with open(outTXTfile, 'w') as f:
        f.write(str(out))

PDFfile = "sample.pdf"
outTXTfile = "pdfoutput.txt"
# pdfToText(PDFfile, outTXTfile) 


# def ConvertImageToTXT(image, txtfile):
#     img = Image.open(image)  
#     output = pytesseract.image_to_string(img)
#     with open(txtfile, 'w') as f:
#         f.write(output)

# image = "sample.png"
# txtfile = "pdfoutput.txt"
# ConvertImageToTXT(image,txtfile)