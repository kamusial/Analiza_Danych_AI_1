import pandas as pd

df = pd.read_csv('data\\cukrzyca_po_obrobce.csv', sep=';')
X = df.iloc[: , :-1]
y = df.outcome

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

