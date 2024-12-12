from Animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, perairan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna= warna
        self.perairan= perairan
    def cetak_ikan(self):
        super().cetak()
        print ("warna \t\t\t:", self.warna,
               "\nperairan \t\t:", self.perairan,
               "\n---------------------------------------")
    