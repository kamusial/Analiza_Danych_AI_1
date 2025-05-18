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

import pandas as pd
def analiza(plik):
    if plik[-4:] == '.csv':
        print('poprawnie rozpoznano format CSV')
    else:
        print('Nie rozpoznano formatu - próbuje csv')
        plik += '.csv'

    dict_data = {}
    df = pd.read_csv(plik)
    print(f'Kształ: {df.shape}')
    dict_data['shape'] = df.shape
    print(f'Nazwy kolumn: {df.columns}')
    dict_data['columns'] = df.columns
    print(f'Pięć pierwszych wierzy: {df.head().to_string()}')
    print(df.describe().T.to_string())
    duplikaty = df.duplicated().sum()
    print(f"Liczba duplikatów przed usunięciem: {duplikaty}")
    print("Brakujące wartości przed uzupełnieniem:")
    print(df.isnull().sum())


    with open('data\\analiza.txt', 'w') as file:
        file.write(f'Kształ: {df.shape}\n')
        file.write(f'Nazwy kolumn: {df.columns}\n')

    return dict_data


