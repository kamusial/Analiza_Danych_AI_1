napis = 'piekna sobota, aby cwiczyc pythona'
print(len(napis))
dlugosc = len(napis)

print(napis[4])  # piąty znak

# liczba liter "a"
# ile jest przecinków
# ile jest spacji

licznik_a = 0
licznik_przecinek = 0
licznik_spacja = 0

for i in range(len(napis)):
    print(f' Analizuje znak {napis[i]}')
    if napis[i] == 'a':
        licznik_a = licznik_a + 1
    if napis[i] == ',':
        licznik_przecinek = licznik_przecinek + 1
    if napis[i] == ' ':
        licznik_spacja = licznik_spacja + 1
print(f'Znaleziono {licznik_a} liter a')
print(f'Znaleziono {licznik_przecinek} przecinkow')
print(f'Znaleziono {licznik_spacja} spacji')





# for i in range(5):
#    print(f'Element nr {i+1} to {i}')
