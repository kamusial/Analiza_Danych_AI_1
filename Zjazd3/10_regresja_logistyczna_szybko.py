import pandas as pd

df = pd.read_csv('data\\cukrzyca_po_obrobce.csv', sep=';')
X = df.iloc[: , :-1]
y = df.outcome

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame( confusion_matrix(y_test, model.predict(X_test) ) ))

print(df.outcome.value_counts())
print('Klasy niezbalaznowane')
print('Zmiana danych')
df1 = df.query('outcome==0').sample(n=500)
df2 = df.query('outcome==1').sample(n=500)
df3 = pd.concat([df1, df2])
# df3 - 1000 rekordów, 500 zdrowych, 500 chorych
X = df3.iloc[: , :-1]
y = df3.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame( confusion_matrix(y_test, model.predict(X_test) ) ))

