
while True:
    passwd = input('Wpisz haslo:   ')
    if passwd == '1234':
        print('Haslo poprawna')
        print('Zapraszamy')
        break
    else:
        print('Zle haslo')
        mother_surname = input('Wpisz nazwisko mamy:  ')
        if mother_surname == 'nowak':
            print('Zapraszamy')
            break

print('Dalsza czesc programu')
