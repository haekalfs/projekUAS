print("-------------------------------------------------------------------")
print("     Welcome to eBPM (enterprises-Business Process Management)")
print("-------------------------------------------------------------------")
Enter = input("Tekan Enter Untuk Melanjutkan...")

from prettytable import PrettyTable
tableInfo = PrettyTable()

tableInfo.field_names = ("ID","Program")
tableInfo.add_row(["BPM1","Pengadaan Barang"])
tableInfo.add_row(["BPM2","Approval Pengadaan Barang"])
tableInfo.add_row(["BPM3","Pembelian Barang"])

print(tableInfo)

userInputChoice = input("Ketik ID Program yang ingin dijalankan...\n")

if (userInputChoice=="BPM1" or userInputChoice=="bpm1"or userInputChoice=="Bpm2"or userInputChoice=="bpM2"or userInputChoice=="BPm2"):
    import classPengadaaneBPM
elif (userInputChoice=="BPM2" or userInputChoice=="bpm2" or userInputChoice=="Bpm2" or userInputChoice=="Bpm2"or userInputChoice=="bpM2"):
    import classApprovaleBPM
elif (userInputChoice=="BPM3" or userInputChoice=="bpm3" or userInputChoice=="Bpm3" or userInputChoice=="bPm3"or userInputChoice=="BPm2"):
    import classPembelianeBPM
else:
    print("Error occured, please try again...")