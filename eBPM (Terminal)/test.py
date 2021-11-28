from prettytable import PrettyTable
tableInfo = PrettyTable()

print("-------------------------------------------------------------------")
print("     Welcome to eBPM (enterprises-Business Process Management)")
print("-------------------------------------------------------------------")
Enter = input("Tekan Enter Untuk Melanjutkan...")

tes = [1,2,3]
tes2 = ["Penjualan Barang"]

tableInfo.field_names = ("ID","Program")
for row in tes:
    tableInfo.add_row([row,"Pengadaan Barang"])

print(tableInfo)