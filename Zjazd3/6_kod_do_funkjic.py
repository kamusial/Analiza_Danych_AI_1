from funkcje import *

print(mnozenie(5, 7))
print(f'Mnozenie 10 i 1.1: {mnozenie(10, 1.1)}')
print(f'Mnozenie 10 i 10: {mnozenie(10, 10)}')
print(f'Mnozenie 100 i 1.1: {mnozenie(100, 1.1)}')


imie = input('Podaj nazwe:  ')
if name_available(imie):
    print('Nazwa uzytkownika wolna')
else:
    print('Nazwa zajęta')


print(skladka(38, 'm', 21, True, 24))
print(skladka(1, 'm', 17, False, 24))