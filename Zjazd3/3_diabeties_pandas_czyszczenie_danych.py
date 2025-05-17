import pandas as pd
import numpy as np

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
    df[col] = df[col].replace(0, np.nan)
    mean_ = df[col].mean()
    df[col].replace(np.nan, mean_, inplace=True)

print('Po obróbce danych')
print(df.describe().T.round(2).to_string())
print(df.isna().sum())

df.to_csv('data\\cukrzyca_po_obrobce.csv', sep=';', index=False)
