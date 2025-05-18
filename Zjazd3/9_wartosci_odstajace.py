from funkcje import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# analiza('data\\otodom.csv')

df = pd.read_csv('data\\otodom.csv')
print(df.describe().T.round(2).to_string())


# sns.heatmap(df.iloc[  :  ,     2:   ].corr(), annot=True)   # pomiń 2 pierwsze kolumny
# plt.show()
#
# sns.histplot(df.cena)
# plt.show()
#
# plt.scatter(df.powierzchnia, df.cena)
# plt.show()

q1 = df.describe().T.loc["cena", "25%"]
q3 = df.describe().T.loc["cena", "75%"]
print(q1, q3)

df1 = df[(df.cena >= q1) & (df.cena <= q3)  ]
print(f'ksztalt {df1.shape}')

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

X = df1.iloc[:, 2:]
y = df1.cena
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

r2 = r2_score(y_test,  model.predict(X_test)  )
print(f'r2: {r2}')

print(pd.DataFrame(model.coef_ , X.columns))
print(f'wyraz wolny: {model.intercept_}')