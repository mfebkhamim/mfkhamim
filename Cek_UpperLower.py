""" aku = "anjaz kelas"
print(str(aku.islower()))

kamu = "Anjaz kelas"
print(str(kamu.islower()))

khamim = "Nope"
print(str(khamim.isupper()))

saya = "WIDIDIW"
print(str(saya.isupper()))

bau = "WIDIDIW"
print(str(bau.isalpha()))

anu = "WIDIDIW"
print(str(anu.isalnum()))

adi = "213124"
print(str(adi.isalnum()))




#Okehhh mantap 


#Format String
nama = 'Khamim'
kode = 'feb'
print("namaku adalah : " + nama + ", dan panggilanku adalah : " + kode)
Format_str = f"namaku adalah : {nama}, dan panggilanku adalah : {kode}"
print(Format_str)

#Tambahin koma atau titik
angka = 20000
Format_str = f"namaku = {angka:,}" 
print(Format_str)

#Ubah bilangan desimal sesuai ketelitian yang diinginkan
angka_desimal = 20000.54321
Format_string = f"bilangannya = {angka_desimal:.3f}" 
print(Format_string)

#Leading zero, gangerti seh iki dingge opo
angka_desimal = 20000.54321
Format_string = f"bilangannya = {angka_desimal:10.3f}" 
print(Format_string)
#Intinya nanti jumlah karakternya bakal 10, semisal kurang akan menjadi spasi di depan / belakang

#Menampilkan plus dan minus
angka_minus = -24
angka_plus = 24

format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.24f}"

print(format_minus)
print(format_plus)

#mengubah ke format persen
persentase = 0.024
format_persen = f"diubah ke persen menjadi = {persentase:.4%}"

print(format_persen)
#jadi akan terubah ke dalam bentuk persen dengan bilangan desimal belakang koma berjumlah 4

#Ubah ke binari, hex, dan oks
print(bin(angka_plus))
print(hex(angka_plus))
print(oct(angka_plus))
"""

'''
def penjumlahan(a, b): 
    c = a + b
    print(f"{a} + {b} = {c}")

penjumlahan(1,2)

def hasil_kuadrat(angka):
	hasil_operasi = angka**2
	return hasil_operasi

x = input("masukkan bilangan yang ingin dikuadratkan : ") 
y = hasil_kuadrat(int(x))
print(f"Maka hasil dari {x}^2 adalah : {y}" ) '''


a = [1, 4, 3, 5,2,3,1,5,7,8,4,2,1,2]
list_a.sort()