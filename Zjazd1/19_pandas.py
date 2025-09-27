import pandas as pd
# from pandas import *

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('weight-height.csv')

print(df)
df.Height *= 2.54
df.Weight /= 2.2
print(df)

# wykresy
# plt.hist(df.Weight, bins=50)
plt.hist(df.query('Gender=="Male"').Weight, bins=50)   # histogram
plt.hist(df.query('Gender=="Female"').Weight, bins=50)   # histogram
plt.show()

# zamiana gender na dane numeryczne
df = pd.get_dummies(df)
del (df['Gender_Male'])
df = df.rename(columns={'Gender_Female': 'Gender'})
print(df)
# 1 - kobieta, 0 - facet

# wejścia: plec, wzrost
# wyście: waga

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(df[["Height", "Gender"]], df["Weight"])
print(f'Test: Waga faceta 190cm: {model.predict([[190, 0]])}\n')
print(f'Współczynnik kierunkowy \"a\": {model.coef_}')
print(f'Wyraz wolny \"b\": {model.intercept_}')

# Własna formuła
wzrost = 180
plec = 0 #facet
waga = wzrost * 1.07 + plec * -8.8 + (-102.5)
print(f'Waga faceta 180cm liczone ręcznie: {waga}')

print(f'Test: Waga faceta 190cm: {model.predict([[190, 0],[190, 1], [100, 0], [50, 1]])}\n')

