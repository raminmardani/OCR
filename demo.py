# importing libraries & packages
import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io
import time

#image to searcheable pdf
PDF = pytesseract.image_to_pdf_or_hocr('invoice-sample.jpg', extension='pdf')
# export to searchable.pdf
with open("searchable_from_image.pdf", "w+b") as f:
    f.write(bytearray(PDF))



#unsearcheable pdf to searcheable pdf
poppler_path = r"C:\Program Files\poppler-22.01.0\Library\bin"
images = convert_from_path('invoice-sample.pdf', poppler_path=poppler_path)
pdf_writer = PyPDF2.PdfFileWriter()
for image in images:
    page = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
    pdf = PyPDF2.PdfFileReader(io.BytesIO(page))
    pdf_writer.addPage(pdf.getPage(0))
with open("searchable_from_pdf.pdf", "wb") as f:
    pdf_writer.write(f)


#mixed searcheable/unsearcheable pdf to searcheable pdf
start = time.time()
poppler_path = r"C:\Program Files\poppler-22.01.0\Library\bin"
images = convert_from_path('combinepdf.pdf', poppler_path=poppler_path)
pdf_writer = PyPDF2.PdfFileWriter()
for image in images:
    page = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
    pdf = PyPDF2.PdfFileReader(io.BytesIO(page))
    pdf_writer.addPage(pdf.getPage(0))
with open("mixed_to_searcheable.pdf", "wb") as f:
    pdf_writer.write(f)
end = time.time()
print(end - start)

#25MB PDF input 80MB output
# runtime: 11minutes
#doesn't mess up when there is mixed pdf pages
#makes searcheable with a good accuracy
#area of improvement: low contrast between text and background