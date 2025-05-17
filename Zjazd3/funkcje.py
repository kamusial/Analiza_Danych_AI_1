def mnozenie(a, b):
    return round(a * b, 4)


userlist = ['Kamil', 'poco123', 'xxx3']
def name_available(name):
    if name not in userlist:
        print('nazwa wolna')
        if len(name) >= 3:
            print('Dlugosc zaakceptowana')
            return True
        else:
            print('nazwa za krotka')
            return False
    else:
        return False


def skladka(wiek, plec, BMI, czy_pali, dlugosc_ubezpieczenia):
    total = 0
    if plec == 'k':
        total += wiek * 5
    elif plec == 'm':
        total += wiek * 6
    else:
        print('Plec nierozpoznana')
        return None
    if BMI > 28:
        total *= 1.2
    if not czy_pali:
        total *= 0.9
    if dlugosc_ubezpieczenia > 11:
        total -= 50
    return total


