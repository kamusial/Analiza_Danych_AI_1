class Auto:
    def __init__(self, barwa, paliwo, wiek):
        self.kolor = barwa
        self.ilosc_paliwa = paliwo
        self.kondycja = 5
        self.tryb_eko = False
        self.spalanie_na_100 = 12
        self.mandaty = []
        self.komentarze = []
        self.rocznik = 2025 - wiek

    def dodaj_mandat(self, info):
        self.mandaty.append(info)

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100
        return round(zasieg * 0.9)

    def ustaw_tryb(self, tryb):
        if tryb == 'eco':
            self.spalanie_na_100 = 8
            self.tryb_ekonomiczny = True
            print('Tryb eco')
        elif tryb == 'normal':
            self.spalanie_na_100 = 12
            self.tryb_ekonomiczny = False
            print('Tryb normal')
        else:
            print('tryb nierozpoznany, brak zmian')


Audi254 = Auto('red', 5, 23)
BWM777 = Auto('black', 50, 0)

print(Audi254.rocznik)
print(BWM777.rocznik)
Audi254.ilosc_paliwa += 20
print(f'Audi ma paliwa: {Audi254.ilosc_paliwa}')
print(Audi254.zasieg())
Audi254.ustaw_tryb('eco')
print(Audi254.zasieg())