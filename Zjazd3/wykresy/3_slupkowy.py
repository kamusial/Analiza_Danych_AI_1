import matplotlib.pyplot as plt
import random

names = ['Ala', 'Ola', 'Kamil', 'Anita', 'Kasia']
points = [random.randint(3, 30) for name in names]

plt.bar(names, points, color=['red', 'green', 'blue'])
plt.xticks(names)
plt.yticks(points)
plt.show()
