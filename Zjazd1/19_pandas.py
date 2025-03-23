import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('weight-height.csv')
print(df)
df.Height *= 2.54
df.Weight /= 2.2
print(df)

# wykresy
plt.hist(df.query('Gender=="Male"').Weight, bins=50)   # histogram
plt.hist(df.query('Gender=="Female"').Weight, bins=50)   # histogram
plt.show()

# zamiana gender na dane numeryczne
df = pd.get_dummies(df)
del (df['Gender_Male'])
df = df.rename(columns={'Gender_Female': 'Gender'})
print(df)

