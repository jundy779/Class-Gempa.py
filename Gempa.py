class Gempa:
    #member1 Variabel
    lokasi = ''
    skla = 0
    #member2 konstruktor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    #member3 method
    def dampak (self):
        if(self.skala < 2): ket = 'Tidak Terasa'
        elif(self.skala >= 2 and self.skala < 4): ket = 'Bagunan Retak-retak'
        elif(self.skala >= 4 and self.skala < 6): ket = 'Bagunan Roboh'
        else: ket = 'Bangunan roboh dan berpotensi tsunami'
        print(
            "========================================",
            "\nINFO   ____                            ",
            "\n      / ___| ___ _ __ ___  _ __   __ _ ",
            "\n     | |  _ / _ \ '_ ` _ \| '_ \ / _` |",
            "\n     | |_| |  __/ | | | | | |_) | (_| |",
            "\n      \____|\___|_| |_| |_| .__/ \__,_|",
            "\n                          |_|          ",
            "\n========================================",
            "\nLokasi Gempa\t:",self.lokasi,
            "\nSkala\t\t\t\t\t:",self.skala,"richter"
            "\nDampak\t\t\t\t:",ket,
            )