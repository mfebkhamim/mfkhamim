import os

def header():
    '''membuat header'''
    os.system("cls")
    print(f"{'--------------------------------------------':^40}") 
    print(f"{'KALKULATOR SEDERHANA' :^40}")
    print(f"{'by : mfkhamim' :^40}")
    print(f"{'--------------------':^40}") 

def hasil_jumlah(angka_1, angka_2):
    return angka_1 + angka_2

def hasil_kurang(angka_1, angka_2):
    return angka_1 - angka_2

def hasil_kali(angka_1, angka_2):
    return angka_1 * angka_2

def hasil_bagi(angka_1, angka_2):
    return angka_1 / angka_2

def hasil_mod(angka_1, angka_2):
    return angka_1 % angka_2

def hasil_pangkat(angka_1, angka_2):
    return angka_1 ** angka_2

def display(angka_pertama, operasi, angka_kedua, hasil):
    print(f"Maka hasil dari {angka_pertama} {operasi} {angka_kedua} = {hasil}")

while True: 
    header()

    angka_pertama = float(input("Masukkan angka pertama : "))
    operasi = input("Masukkan jenis operasi (+,-,/,*,%,^) : " )
    angka_kedua = float(input("Masukkan angka kedua : "))

    if operasi == "+":
        hasil = hasil_jumlah(angka_pertama, angka_kedua)
        display(angka_pertama, operasi, angka_kedua, hasil)
    elif(operasi == "-"):
        hasil = hasil_kurang(angka_pertama, angka_kedua)
        display(angka_pertama, operasi, angka_kedua, hasil)
    elif(operasi == "*"):
        hasil = hasil_kali(angka_pertama, angka_kedua)
        display(angka_pertama, operasi, angka_kedua, hasil)
    elif(operasi == "/"):
        hasil = hasil_bagi(angka_pertama, angka_kedua)
        display(angka_pertama, operasi, angka_kedua, hasil)
    elif(operasi == "%"):
        hasil = hasil_mod(angka_pertama, angka_kedua)
        display(angka_pertama, operasi, angka_kedua, hasil)
    elif(operasi == "^"):
        hasil = hasil_pangkat(angka_pertama, angka_kedua)
        display(angka_pertama, operasi, angka_kedua, hasil)
    else:
        print("Operator yang anda masukkan invalid!")


    isContinue = input(f"Apakah lanjut (y/n)? ")
    if isContinue.lower() == "n":
        break

print("Program telah selesai, thanks!")