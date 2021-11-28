from prettytable import PrettyTable
tableInfo = PrettyTable()

print("-------------------------------------------------------------------")
print("     Welcome to eBPM (enterprises-Business Process Management)")
print("-------------------------------------------------------------------")
Enter = input("Tekan Enter Untuk Melanjutkan...")

tes = [1]
tes2 = ["Penjualan Barang"]

tableInfo.field_names = ("ID","Program")
tableInfo.add_row(["BPM1","Pengadaan Barang"])
tableInfo.add_row(["BPM2","Approval Pengadaan Barang"])
tableInfo.add_row(["BPM3","Pembelian Barang"])
tableInfo.add_row([tes,', '.join(tes2)])

print(tableInfo)