import pandas as pd
from pyexpat import features
from ucimlrepo import fetch_ucirepo
from sklearn.preprocessing import StandardScaler

# fetch dataset
wine_quality = fetch_ucirepo(id=186)

# data (as pandas dataframes)
X = wine_quality.data.features
y = wine_quality.data.targets

# metadata
print(wine_quality.metadata)

# variable information
print(wine_quality.variables)

print('Analiza')
print(wine_quality.data.features.describe().T.to_string())
print('Pokaż tylko mean i std')
print(wine_quality.data.features.describe().loc[['mean', 'std']].T.to_string())
print('Standaryzacja')

X = wine_quality.data.features.values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_scaled = pd.DataFrame(X_scaled, columns=wine_quality.data.features.columns)
print(X_scaled)
print(X_scaled.describe().T.to_string())
X = X_scaled

print(y.value_counts())

# dane ustandaryzowane albo nieustandaryzowane - dalej można wejśc w ML