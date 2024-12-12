import Hitung
import LuasBangunDatar as bangundatar
import LuasBangunRuang as bangunruang

#Modul Hitung
print("========== Modul Hitung =========")
Hitung.tambah(8,1)
Hitung.kurang(10,7)
Hitung.kali(9,6)
Hitung.bagi(15,3)
Hitung.pangkat(7,2)

#Modul Luas Bangun Datar
print("========== Modul LuasBangunDatar =========")
bangundatar.l_persegi(8)
bangundatar.l_persegipanjang(12,6)
bangundatar.l_segitiga(4,8)
bangundatar.l_lingkaran(7)
bangundatar.l_jajargenjang(8,9)

#Modul Luas Bangun Ruang
print("========== Modul LuasBangunRuang =========")

bangunruang.l_balok(2,4,8)
bangunruang.l_prismasegitiga(3,9,7)
bangunruang.l_limas(8,6)
bangunruang.l_tabung(7,10)
bangunruang.l_kubus(8)

