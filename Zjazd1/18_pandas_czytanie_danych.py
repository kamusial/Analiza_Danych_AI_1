import pandas
import math

df = pandas.read_csv('heart.csv', comment='#')
print(df)
print(type(df))
print(df.head(3))
print(df.describe().T.to_string())

df['slope'] += 5
df['nowe_dane'] = df['chol'] * 15 - df['age']
del df['cp']
print(df)