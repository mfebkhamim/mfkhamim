angka = input('masukkan sebarang angka : ')
Wadah = 0

angka = int(angka)

while angka > 0 :
    Wadah = Wadah + angka%10
    angka = angka // 10

print(int(Wadah))