from funkcje import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# analiza('data\\otodom.csv')

df = pd.read_csv('data\\otodom.csv')
print(df.describe().T.round(2).to_string())


sns.heatmap(df.iloc[  :  ,     2:   ].corr(), annot=True)   # pomiń 2 pierwsze kolumny
plt.show()

sns.histplot(df.cena)
plt.show()

plt.scatter(df.powierzchnia, df.cena)
plt.show()

q1 = df.describe().T.loc["cena", "25%"]
q3 = df.describe().T.loc["cena", "75%"]
print(q1, q3)

df1 = df[(df.cena >= q1) & (df.cena <= q3)  ]
print(f'ksztalt {df1.shape}')

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X = df1.iloc[:, 2:]
y = df1.cena
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

