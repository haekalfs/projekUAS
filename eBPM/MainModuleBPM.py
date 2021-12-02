#Kodingan dibawah adalah kodingan untuk import & menampilkan data menjadi sebuah table, sejenis pandas
from prettytable import PrettyTable
tableInfo = PrettyTable()

#kodingan dibawah hanya untuk hiasan, tidak ada fungsi, variable Enter dibawah pun unused/tidak dipakai
print("-------------------------------------------------------------------")
print("     Welcome to eBPM (enterprises-Business Process Management)")
print("-------------------------------------------------------------------")
Enter = input("Tekan Enter Untuk Melanjutkan...")

#kodingan dibawah ini adalah lanjutan kodingan dipaling atas, setelah import pretty table kemudian kita -
# - input data nya kedalam pretty table
tableInfo.field_names = ("ID","Program")
tableInfo.add_row(["BPM1","Pengadaan Barang"])
tableInfo.add_row(["BPM2","Approval Pengadaan Barang"])
tableInfo.add_row(["BPM3","Credits"])
#menampilkan tablenya dengan print(variableTablenya)
print(tableInfo)

#kodingan dibawah adalah user input, jd user akan disuruh input, dmn inputan ini nantinya akan dipakai untuk logic
#if statement
userInputChoice = input("Ketik ID Program yang ingin dijalankan...\n")

#dibawah adalah kodingan if statement, dimana jika user input bpm1 maka user akan menjalankan program bpm1/classPengadaaneBPM.py
#dan jika user input bpm2 maka user akan menjalankan program bpm2/classApprovaleBPM.py
# terakhir jika user input bpm3 maka user akan menjalankan program/class bpm2/classCreditseBPM.py
if (userInputChoice=="BPM1" or userInputChoice=="bpm1"or userInputChoice=="Bpm1"or userInputChoice=="bpM1"or userInputChoice=="BPm1"):
    import classPengadaaneBPM
elif (userInputChoice=="BPM2" or userInputChoice=="bpm2" or userInputChoice=="Bpm2" or userInputChoice=="Bpm2"or userInputChoice=="bpM2"):
    import classApprovaleBPM
elif (userInputChoice=="BPM3" or userInputChoice=="bpm3" or userInputChoice=="Bpm3" or userInputChoice=="bPm3"or userInputChoice=="BPm3"):
    import classCreditseBPM
else:
    print("Error occured, please try again...")




""" Copyright to Haekal Sastradilaga"""