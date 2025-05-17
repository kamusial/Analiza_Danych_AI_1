def mnozenie(a, b):
    return round(a * b, 4)


print(mnozenie(5, 7))
print(f'Mnozenie 10 i 1.1: {mnozenie(10, 1.1)}')
print(f'Mnozenie 10 i 10: {mnozenie(10, 10)}')
print(f'Mnozenie 100 i 1.1: {mnozenie(100, 1.1)}')


userlist = ['Kamil', 'poco123', 'xxx3']
def name_available(name):
    if name not in userlist and len(name) >= 3:
        return True
    else:
        return False

imie = input('Podaj nazwe:  ')
if name_available(imie):
    print('Nazwa uzytkownika wolna')
else:
    print('Nazwa zajęta')

