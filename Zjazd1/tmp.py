licznik = 0
for i in range(20):
    if i % 2 == 0:
        print(f'{i} jest liczba parzysta')
    else:
        print(f'{i} jest liczba NIEparzysta')

    if i >= 2 and i <= 5:
        print(f'Ocena {i} jest poprawna')
    else:
        print(f'Ocena {i} jest NIEpoprawna')

    if i % 7 == 0:
        licznik = licznik + 1
        print(f'Liczba {i} jest podzielna przez 7')
        print(f'Na razie mamy {licznik} liczb podzielnych przez 7')

print(f'Mamy {licznik} liczb podzielnych przez 7')
print('Koniec programu')