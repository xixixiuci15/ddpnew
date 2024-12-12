from Animal import Animal

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, ukuran, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.ukuran= ukuran
        self.bunyi= bunyi
    def cetak_burung(self):
        super().cetak()
        print ("ukuran \t\t\t:", self.ukuran,
               "\nbunyi \t\t\t:", self.bunyi,
                "\n---------------------------------------")
    
