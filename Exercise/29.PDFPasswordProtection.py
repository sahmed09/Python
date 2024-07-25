from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

# Open the PDF
file_pdf = PdfReader('Datasets/keyboard-shortcuts-suggested-list.pdf')
print(file_pdf)
print(len(file_pdf.pages))

# Object for PDF Writer
pdf_writer = PdfWriter()

for i in range(len(file_pdf.pages)):
    page_details = file_pdf.pages[i]
    # Add to the out page
    pdf_writer.add_page(page_details)

password = '123456'

pdf_writer.encrypt(password)

with open('Datasets/encrypted_keyboard_shortcuts.pdf', 'wb') as filename:
    pdf_writer.write(filename)
