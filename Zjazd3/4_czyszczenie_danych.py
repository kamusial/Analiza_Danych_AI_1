import pandas as pd

df = pd.read_csv('data\\retail_store_sales.csv')

print(f'Kształt danych: {df.shape}')
print(f'Nazwy kolumn: {df.columns}')
print(f'Pięć pierwszych wierzy: {df.head().to_string()}')
print(df.describe().T.to_string())

duplikaty = df.duplicated().sum()
print(f"Liczba duplikatów przed usunięciem: {duplikaty}")
df = df.drop_duplicates()
print(f"Liczba wierszy po usunięciu duplikatów: {df.shape[0]}")

df['Category'] = df['Category'].str.strip()
df['Category'] = df['Category'].str.capitalize()
print(f'Pięć pierwszych wierzy po czyszczeniu: {df.head().to_string()}')

