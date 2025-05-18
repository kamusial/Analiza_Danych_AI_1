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
print('Skalowanie')
