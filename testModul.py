from fpdf import FPDF

a = input("a")
b = input("b")
aa = ("No PO :", a)
def createPDF():
    pdf = FPDF()
    # Add a page
    pdf.add_page()
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
    # create a cell
    pdf.cell(200, 10, txt = "Form Pengadaan eBPM", 
            ln = 1, align = 'C')
    
    pdf.cell(200, 10, txt = "Kelompok 1 19.1C.11 UBSI",
            ln = 2, align = 'C')

    pdf.cell(200, 10, txt = "--------------------------------------------",
         ln = 10, align = 'C')
    
    pdf.cell(200, 10, txt = (str(b)),
            ln = 12, align = 'C')
    pdf.cell(200, 10, txt = (str(b)),
            ln = 12, align = 'B')
            
    # save the pdf with name .pdf
    pdf.output("Form Pengadaan.pdf") 

createPDF()

"""""
# importing all the required modules
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
fileReader = PyPDF2.PdfFileReader(file_path)

file_path2 = filedialog.askopenfilename()
fileReader2 = PyPDF2.PdfFileReader(file_path2)

output = PdfFileWriter()

output.addPage(fileReader.getPage(0))
output.addPage(fileReader2.getPage(0))

outputStream = open(r"output.pdf", "wb")
output.write(outputStream)
outputStream.close()"""