#ini kodingan untuk import lib package, pretty table, dan fpdf untuk generate pdf otomatis
from prettytable import PrettyTable
from fpdf import FPDF
tblForm = PrettyTable()

#ini variable list
listProcurement = []
totalHarga = []

#kemudian ada class PengadaanBarang, dimana ini adalah kodingan user input & appending ke list
class PengadaanBarang:
    def barang(brg):
        global noPO
        global namaProduk
        global jumlahProduk
        global danaRequested
        global hargaBarang
        print("-------------------------------------------------------------------")
        print("                          eBPM Procurement")
        print("-------------------------------------------------------------------")
        noPO = input("Input Nomor PO (Purchase Order)... Exp : (001,002...)\n")
        namaProduk = input("Input Nama Barang yang akan diadakan : ")
        jumlahProduk = int(input("Input Jumlah Barang               : "))
        hargaBarang = int(input("Input Harga Satuan Barang         : "))
        danaRequested = int(input("Input Dana yang direquest         : "))
        print("-------------------------------------------------------------------\n")
        totalHarga.append(hargaBarang * jumlahProduk)                                                           #hitung total harga dan ditambahkan ke list diatas "totalHarga"
        #kodingan dibawah fungsinya untuk insert data ke pretty table, tblform field names untuk baris atasnya
        tblForm.field_names = ("Nomor PO", "Nama Barang", "Jumlah", "Harga Satuan", "Dana Requested")
        tblForm.add_row([noPO,namaProduk,jumlahProduk,'{:,}'.format(hargaBarang),'{:,}'.format(danaRequested)])

#ini fungsi nya untuk generate pdf setelah kita melakukan user input, umpamanya seperti adanya invoice setelah pembelian barang
def createPDF():
    global pdf
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)

    pdf.cell(200, 10, txt = "Form Pengadaan eBPM", 
            ln = 1, align = 'C')
    
    pdf.cell(200, 10, txt = "Kelompok 1 19.1C.11 UBSI",
            ln = 2, align = 'C')

    pdf.cell(200, 20, txt = "________________________________________________________________",
         ln = 10, align = 'A')

    pdf.cell(200, 10, txt = "Nomor PO :",
            ln = 11, align = 'A')
    
    pdf.cell(200, 10, txt = noPO,
            ln = 11, align = 'A')

    pdf.cell(200, 10, txt = "Nama Produk :",
            ln = 13, align = 'A')
    
    pdf.cell(200, 10, txt = namaProduk,
            ln = 13, align = 'A')

    pdf.cell(200, 10, txt = "Jumlah Produk :",
            ln = 15, align = 'A')
    
    pdf.cell(200, 10, txt = str('{} - pcs'.format(jumlahProduk)),
            ln = 15, align = 'A')

    pdf.cell(200, 10, txt = "Harga Produk :",
            ln = 17, align = 'A')
    
    pdf.cell(200, 10, txt = str('Rp. {:,}'.format(hargaBarang)),
            ln = 17, align = 'A')

    pdf.cell(200, 10, txt = "Dana Request :",
            ln = 19, align = 'A')
    
    pdf.cell(200, 10, txt = str('Rp. {:,}'.format(danaRequested)),
            ln = 19, align = 'A')

    pdf.cell(200, 10, txt = "________________________________________________________________",
         ln = 20, align = 'A')
    pdf.cell(200, 10, txt = "Copyright to : Mahasiswa UBSI",
            ln = 21, align = 'C')

#kodingan dibawah fungsinya untuk menjalankan kodingan secara ber-urutan, dan kita tinggal panggil fungsi ini startProgram()
# maka dia akan running fungsi" diatas secara berurutan

def startProgram():
    for i in range(jumlahPengadaan):                                                    #pertama dia akan running looping
        print ("\nForm Pengadaan ke - " + str(i+1))
        PengadaanBarang().barang()                                                      #kedua dia akan memanggil Class "PengadaanBarang"
        Sum = sum(totalHarga)                                                           #ketiga dia akan menghitung jumlah di list totalHarga
        createPDF()                                                                     # keempat kita atur biar dia generate pdf dengan memanggil fungsi def createPDF()
        pdf.output('eBPM/outputFormPengadaan/Form Pengadaan eBPM' + str(i) + '.pdf')    #terakhir kita cetak pdfnya
    #Output
    print("\nComputing... Please Wait... Creating Form....")
    print("-------------------------------------------------------------------")
    print("                         eBPM Procurement")
    print("-------------------------------------------------------------------")
    print(tblForm)
    print("Total Biaya Pengadaan Barang : Rp.",'{:,}'.format(Sum))
    print("Thank You For Using Our Program, Please wait for Approval by Directors.\n")

#kode dibawah adalah tampilan awal program
print("-------------------------------------------------------------------")
print("                    Welcome to eBPM Procurement")
print("-------------------------------------------------------------------")

enter = input("Apakah anda yakin ingin melakukan pengadaan barang?...(Y/N)\n")          #jika user tekan y maka program jalan jika n maka akan gagal
jumlahPengadaan = int(input("Berapa form pengadaan barang?...\n"))                      #ini fungsinya untuk user input brp bnyk form yang mau diinput

print("\nLoading...")

#Running Program dengan if statement, jika user input y maka program jalan, selain itu user akan stop programnnya
if(enter=="Y" or enter=="y"):
    startProgram()
else:
    print("Thank you for using our program... Good Bye...")





""" Copyright to Haekal Sastradilaga"""