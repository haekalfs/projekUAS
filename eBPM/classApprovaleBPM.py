#Import library package
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
#package lib dibawah ini fungsinya untuk menampilkan popup choose a file, jd kita bisa pilih file di komputer
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

#tampilan awal
print("-------------------------------------------------------------------")
print("                    Welcome to eBPM Approval")
print("-------------------------------------------------------------------")

#kuesioner untuk user, yg nntinya akan menentukan apakah user ingin menjalankan program atau tidak
enter = input("Tekan enter untuk melanjutkan...\n")
userChoice = input("Apakah anda ingin melakukan proses Approval 'Pengadaan Barang'?...(Y/N) :")
print("-------------------------------------------------------------------")
print("Pilih File Form Cetak Pengadaan Barang Yang Ingin di Approve...\n")

#jika user pilih Y maka user akan dimunculkan POPUP menu dimana user disuruh pilih file yang ingin di approve
if(userChoice=="Y" or userChoice=="y"):
    #dua baris dibawah adalah popup menu
    file_path = filedialog.askopenfilename()
    fileReader = PyPDF2.PdfFileReader(file_path) #read file yang dipilih
    #dua baris dibawah hanya hiasan
    print("Please Wait... Creating Form...\n")
    print("Approving Form... Creating Sign...\n")
    #baris dibawah fungsinya untuk read file approve.pdf, yang nntinya akan di gabungkan ke file yg user pilih tadi
    pdfTwo = PyPDF2.PdfFileReader(open("eBPM/approve.pdf", "rb"))
    #variable output, untuk write file pdf
    output = PdfFileWriter()
    #output akan menggabungkan file approve.pdf dengan file yang user pilih td
    output.addPage(pdfTwo.getPage(0))#approve.pdf
    output.addPage(fileReader.getPage(0))#file user

    #variable outputStream fungsinya untuk menentukan letak folder yang nntinya akan jd tmpat file pdf baru
    outputStream = open(r"eBPM/outputFormApproval/Form Pengadaan (Approved).pdf", "wb")
    #baris dibawah untuk men save file pdf yg digabungkan td ke folder outputStream
    output.write(outputStream)
    outputStream.close() #close
    print("-------------------------------------------------------------------")
    print("File telah tersimpan di folder program eBPM...")
    print("Thank you for using our program...")
    print("-------------------------------------------------------------------") #selesai
elif(userChoice=="N" or userChoice=="n"):
    print("Thank you for using our program...")
else:
    print("Please input y/N as instructed...")







""" Copyright to Haekal Sastradilaga"""