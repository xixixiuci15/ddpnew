from Burung import *
from Ikan import *
from Ular import *

cobra = Ular("cobra", "tikus", "sawah", "Bertelur", "hitam polos", "beracun")
sanca = Ular("sanca", "ayam", "rawa-rawa", "Bertelur", "batik", "tidak beracun")
salmon = Ikan("Salmon", "larva", "air", "Bertelur", "silver", "sungai")
cupang = Ikan("cupang", "pelet", "air", "Bertelur", "biru", "aquarium")
lovebird = Burung("lovebird", "biji2an", "udara", "Bertelur", "kecil", "cicitcuit")
kakaktua = Burung("kakaktua", "jagung", "udara", "Bertelur", "sedang", "clamatpagi")

sanca.cetak_ular()
cobra.cetak_ular()
cupang.cetak_ikan()
salmon.cetak_ikan()
lovebird.cetak_burung()
kakaktua.cetak_burung()

