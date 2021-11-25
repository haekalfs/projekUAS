from prettytable import PrettyTable
import mysql.connector

tblBrg = PrettyTable()

print("-------------------------------------------------------------------")
print("                    Welcome to eBPM Pembelian")
print("-------------------------------------------------------------------")

userChoice = input("Apakah anda sudah melakukan Request Pengadaan Barang?...(Y/N)\n")

enter = input("Tekan enter untuk melanjutkan...\n")

class PembelianBarang:
    def beli(self):
            print("Beli Barang")