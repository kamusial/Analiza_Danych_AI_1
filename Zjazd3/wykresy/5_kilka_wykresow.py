import matplotlib.pyplot as plt
import random
import math

X = [x for x in range(0, 360+1, 10)]
Y1 = [math.cos(math.radians(i)) for i in X]
Y2 = [random.random() for i in X]

plt.subplot(1, 2, 1)
plt.plot(X,Y1,"r.-")
plt.subplot(1, 2, 2)
plt.plot(X,Y2,"bs:")
plt.show()