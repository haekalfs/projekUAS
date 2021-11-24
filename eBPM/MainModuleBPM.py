print("Welcome to e-BPM")
Enter = input("Tekan Enter Untuk Melanjutkan...")

from prettytable import PrettyTable
tableInfo = PrettyTable()

tableInfo.field_names = ("ID","Program")
tableInfo.add_row(["BPM1","Pengadaan Barang"])
tableInfo.add_row(["BPM2","Approval Pengadaan Barang"])
tableInfo.add_row(["BPM3","Pembelian Barang"])

print(tableInfo)

userInputChoice = input("Ketik ID Program yang ingin dijalankan...")

if (userInputChoice=="BPM1" or userInputChoice=="bpm1\n"):
    from classPengadaaneBPM import PengadaanBarang
elif (userInputChoice=="BPM2" or userInputChoice=="bpm2"):
    print()
elif (userInputChoice=="BPM2" or userInputChoice=="bpm2"):
    print()
else:
    print("Error occured, please try again...")