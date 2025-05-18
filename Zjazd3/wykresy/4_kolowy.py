import matplotlib.pyplot as plt

wydatki = ['mieszkanie', 'media', 'rozrywka', 'nauka', 'pokemony']
values = [2000, 400, 120, 700, 1230]
explode = [0 for i in wydatki]
explode[wydatki.index('nauka')] = 0.3
plt.pie(values, labels=wydatki, explode=explode, shadow=True)
plt.show()