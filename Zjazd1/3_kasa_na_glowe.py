# program pyta o zarobki i liczbe dzieci
# obowiazuje 800+ na kazde dziecko
# zarobki:
# pow 5000 - podatek 20%
# 3000 - 5000 - podatek 10%
# ponizej 3000 - brak podatku
# program zwraca kwote na osobe w rodzinie

zarobki = int(input('Ile zarabiasz?   '))
liczba_dzieci = int(input('Ile masz dzieci?   '))
liczba_osob = liczba_dzieci + 2
if zarobki > 5000:
    zarobki_netto = zarobki * 0.8
elif zarobki >= 3000:
    zarobki_netto = zarobki * 0.9
else:
    zarobki_netto = zarobki
kasa_total = zarobki_netto + liczba_dzieci * 800
kasa_na_glowe = kasa_total / liczba_osob
print(f'W rodzinie na osobe {kasa_na_glowe}')
