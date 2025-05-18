from funkcje import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# analiza('data\\otodom.csv')

df = pd.read_csv('data\\otodom.csv')
print(df.describe().T.round(2).to_string())


sns.heatmap(df.iloc[  :  ,     1:   ].corr(), annot=True)   # pomiń pierwszą kolumne
plt.show()
