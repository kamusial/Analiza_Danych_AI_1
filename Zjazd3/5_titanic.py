import pandas as pd
import numpy as np

df = pd.read_csv('data\\train.csv')
print(f'Kształt danych: {df.shape}')
print(df.describe().T.to_string())
print(df.head(5).to_string())
print("Brakujące wartości przed uzupełnieniem:")
print(df.isnull().sum())

median_age = df['Age'].median(skipna=True)
print(f"Mediana wieku: {median_age:.2f}")
df['Age'] = df['Age'].fillna(median_age)

most_common_port = df['Embarked'].mode()[0]
print(f"Najczęstszy port zaokrętowania: {most_common_port}")
df['Embarked'] = df['Embarked'].fillna(most_common_port)

perc_cabin_missing = df['Cabin'].isnull().mean() * 100
print(f'proecnt brakujących kabin: {perc_cabin_missing}')
if perc_cabin_missing > 50:
#    del df['Cabin']
    df = df.drop('Cabin', axis=1)
    print("Kolumna 'Cabin' została usunięta ze względu na zbyt wiele brakujących danych.")

print('Weryfikacja')
print(df.isnull().sum())