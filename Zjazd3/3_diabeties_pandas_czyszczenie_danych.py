import pandas as pd

df = pd.read_csv("data\\diabetes.csv")
print(f'kształanych: {df.shape}')
print(df.describe().T.round(2).to_string())
print('Braki')
print(df.isna().sum())

# dla każej kolumny z brakami,
# tam, gdzie 0 bądźbrak wartości
# wpisz średnią dla danej kolumny (bez zer)

print(f'Nazwy kolumn: {df.columns}')

for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin',
       'bmi', 'diabetespedigreefunction', 'age']:
    df[col]
    # zamień zera na brak wartości
    # policz średnią
    # wpisz średnia, tam, gdzie brak wartości