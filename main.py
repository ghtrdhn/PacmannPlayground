from bis import Bis
import numpy


bis_utama = Bis(10, 0, 10_000)
print("Selamat datang di sistem bis terotomasi")

while(True):
    print("Menu: ")
    print("1. Scan-in")
    print("2. Scan-out")
    print("3. Keluar Program")

    menu = input("Masukan pilihan: ")

    if menu == "1":
        #proses scan-in
        id = input("Masukan id penumpang yang ingin naik bis: ")
        nama = input("Masukan nama penumpang yang ingin naik bis: ")
        bis_utama.scan_in(id,nama)
        
    elif menu =="2":
        #proses scan-out
        id = input("Masukan id penumpang yang ingin turun dari bis: ")
        bis_utama.scan_out(id)
    elif menu =="3":
        #Keluar program
        exit()
    else:
        print("Pilihan Salah")
    

