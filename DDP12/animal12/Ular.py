from Animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.corak= corak
        self.racun= racun
    def cetak_ular(self):
        super().cetak()
        print ("corak \t\t\t:", self.corak,
               "\njenis racun \t\t:", self.racun,
                "\n---------------------------------------")
    
