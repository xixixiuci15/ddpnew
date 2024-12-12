import math

def l_kubus(rusuk):
    hitung = 6 * rusuk * rusuk
    print(f'luas kubus adalah {hitung}')

def l_balok(p, l, t):
    hitung = 2 * (p*l)+(p*t)+(l*t)
    print(f'luas balok adalah {hitung}')

def l_prismasegitiga(luas, keliling, tinggi):
    hitung = 2 * luas + keliling * tinggi 
    print(f'luas prisma segitiga adalah {hitung}')

def l_limas(luas, luassisi ):
    hitung = luas + luassisi
    print(f'luas limas adalah {hitung}')

def l_tabung(r, t):
    hitung = 2 *3.14 * r * (r + t)
    print(f'luas tabung adalah {hitung} ')
