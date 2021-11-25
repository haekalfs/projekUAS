from prettytable import PrettyTable
import mysql.connector

tblList = PrettyTable()

print("-------------------------------------------------------------------")
print("                    Welcome to eBPM Approval")
print("-------------------------------------------------------------------")

userChoice = input("Apakah anda ingin melakukan proses Approval Pengadaan Barang?...(Y/N)\n")

enter = input("Tekan enter untuk melanjutkan...\n")

class ApprovalBarang:
    def sqlQueryRead(qry):
            global pick
            global userPick
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='ebpm',
                                                    user='root',
                                                    password='password')

                sql_select_Query = "select * from penjualankelompok1"
                cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                print("Jumlah List Pengadaan Barang yang direquest :", cursor.rowcount)

                print("\nPrinting....")
                tblList.field_names = ("ID","Nomor PO", "Nama Barang", "Jumlah", "Dana Requested", "Harga Produk", "status")
                for row in records:
                    tblList.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
                print(tblList)

            except mysql.connector.Error as e:
                print("Error reading data from MySQL table", e)
            finally:
                if connection.is_connected():
                    connection.close()
                    cursor.close()
            userPick = 0
            pick = input("\nApakah anda director? : ")
            userPick = int(input("\nPilih ID Table untuk diApprove : "))

    def ifLogicSelectingTbl(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                        database='ebpm',
                                                        user='root',
                                                        password='password')

            cursor = connection.cursor()
            sql_Delete_query = """UPDATE penjualankelompok1 SET status='Approved' where id = %s"""
            # row to delete
            cursor.execute(sql_Delete_query, (userPick,))
            connection.commit()
            print("Procurement Approved successfully ")

        except mysql.connector.Error as error:
            print("Failed to Edit record from table: {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

##start program with inheritance

if(userChoice=="Y" or userChoice=="y"):
    ApprovalBarang().sqlQueryRead()
    if(pick=="Y" or pick=="y"):
        ApprovalBarang().ifLogicSelectingTbl()
elif(userChoice=="N" or userChoice=="n"):
    print("Thank you for using our program...")