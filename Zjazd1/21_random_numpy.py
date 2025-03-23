# Napisz program, który wygeneruje jednowymiarową tablicę losowych liczb całkowitych z zakresu od 1 do 50 o długości 10 elementów.
# Następnie wykonaj:
#
# Obliczenie średniej arytmetycznej wygenerowanych liczb.
# Znalezienie najmniejszej i największej wartości.
# Wybór jednej losowej wartości z wygenerowanej tablicy przy użyciu biblioteki random.

import random
import numpy as np
from numpy.ma.core import minimum_fill_value

numbers = np.random.randint(1, 50, size=10)
print(f'wygenerowane dane: {numbers}')

average = np.mean(numbers)
print(f'Srednia: {average}')

min_value = np.min(numbers)
max_value = np.max(numbers)

print(f'Minimum: {min_value}, maximum: {max_value}')

random_number = random.choice(numbers)
print(f'Losowa wartość: {random_number}')