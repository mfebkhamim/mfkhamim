print("hello world!")

age = input("Masukkan usia anda : ")

print('Umur anda adalah ' + age + ' tahun')

age = int(age)

if age > 0 and age <= 13 :
    print('Anda Anak-anak')
elif age > 13 and age <= 20 : 
    print('Anda Remaja')
elif age > 20 and age <=55 : 
    print('Anda Dewasa')
elif age > 55 : 
    print('Anda Manula')
else :
    print('input anda tidak valid')