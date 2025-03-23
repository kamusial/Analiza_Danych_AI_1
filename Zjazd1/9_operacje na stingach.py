imie = 'Kamil'
nazwisko = 'Musial'
nazwa_firmy = 'merito'

mail = imie + '.' + nazwisko+ '@' + nazwa_firmy +'.pl'

print(f'Witaj {imie}, masz maila {mail}')

employees_list = [
    ['Marek', 'Siwek', 34],
    ['Kasia', 'Banach', 42],
    ['Mariusz', 'Nowak', 2]
                    ]

print(f'Drugi pracownik na liscie to: {employees_list[1]}')
print(f'Nazwisko 3go pracownika to {employees_list[2][1]}')

# dla listy pracownikow, napisac powitanie, stworzyc maila, napisac ile dni urlopu

for emp in employees_list:
    if emp[0][-1] == 'a':
        print(f'Szanowna Pani {emp[0]}')
    else:
        print(f'Szanowny Pan {emp[0]}')
    if emp[2] > 10:
        print('Masz 26 dni urlopu')
    else:
        print('Masz 20 dni urlopu')
    print(f"twoj mail to: {emp[0]+'.'+emp[1]+'@merito.pl'}")