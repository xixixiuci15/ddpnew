print('\n----mencari celcius ke fahrenheit----')
def celcius_ke_fahrenheit(celcius):
     fahrenheit = (celcius *9/5) + 32
     return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))


print('\n----mencari bilangan genap----')
def is_genap(bil_genap):
      return bil_genap %2 == 0
#untuk memasukan value 
print (is_genap(4))
print (is_genap(7))


print('\n----mencetak nilai kelulusan----')
#rata-rata nilai 70
def nilai_kelulusan(nilai):
 if nilai >=80:
   return'Lulus'
 else:
   return'Tidak Lulus'
#untuk mencetak value
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))

print('\n----cetak bilangan genap----')
def bil_ganjil(angka):
   for i in range (1, angka, 2):
    print(i, end=" ")
    #untuk memasukan value 
bil_ganjil(20)