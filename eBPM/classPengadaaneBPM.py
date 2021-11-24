from prettytable import PrettyTable
tblForm = PrettyTable()

print("-------------------------------------------------------------------")
print("                    Welcome to eBPM Procurement")
print("-------------------------------------------------------------------")

enter = input("Apakah anda yakin ingin melakukan pengadaan barang?...(Y/N)\n")
jumlahPengadaan = int(input("Berapa form pengadaan barang?...\n"))

print("\nLoading...\n")

listProcurement = []
totalHarga = []

class PengadaanBarang:
    def barang(brg):
        global totalHarga
        global tblForm
        print("-------------------------------------------------------------------")
        print("                          eBPM Procurement")
        print("-------------------------------------------------------------------")
        noPO = input("Input Nomor PO (Purchase Order)... Exp : (001,002...)\n")
        namaProduk = input("Input Nama Barang yang akan diadakan : ")
        jumlahProduk = int(input("Input Jumlah Barang               : "))
        hargaBarang = int(input("Input Harga Satuan Barang         : "))
        danaRequested = int(input("Input Dana yang direquest         : "))
        print("-------------------------------------------------------------------\n")
        totalHarga.append(hargaBarang * jumlahProduk)
        tblForm.field_names = ("Nomor PO", "Nama Barang", "Jumlah", "Harga Satuan", "Dana Requested")
        tblForm.add_row([noPO,namaProduk,jumlahProduk,'{:,}'.format(hargaBarang),'{:,}'.format(danaRequested)])
    
def startProgram():
    for i in range(jumlahPengadaan):
        print ("Form Pengadaan ke - " + str(i+1))
        PengadaanBarang().barang()
        Sum = sum(totalHarga)
    print("\nComputing... Please Wait... Creating Form....")
    print("-------------------------------------------------------------------")
    print("                         eBPM Procurement")
    print("-------------------------------------------------------------------")
    print(tblForm)
    print("Total Biaya Pengadaan Barang : Rp.",'{:,}'.format(Sum))
    print("Thank You For Using Our Program, Please wait for Approval by Directors.\n")

if(enter=="Y" or enter=="y"):
    startProgram()
else:
    print("Thank you for using our program... Good Bye...")