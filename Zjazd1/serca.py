import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('heart.csv', comment='#')

print(df.target.value_counts())

X = df.iloc[: , :-1]
y = df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.model_selection import GridSearchCV
model = DecisionTreeClassifier()
#criterion: This parameter specifies the function to measure the quality of a split. Supported criteria are "gini" for the Gini impurity and "entropy" for the information gain.
params = {
    "criterion": ["gini", "entropy", "log_loss"],
    "max_depth" : range(3,14),
    "max_features" : range(5, X_train.shape[1]+1,2),
    "min_samples_split" : [2, 3, 4, 5]
}

grid = GridSearchCV(model, params, scoring="accuracy", cv=10, verbose=2)
grid.fit(X_train, y_train)

print(grid.best_params_)
print(grid.best_score_)
print(grid.best_estimator_)




#