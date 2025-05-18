import matplotlib.pyplot as plt

# funkcja 1: y = 5x - 2 ; funkcja 2: y = -2x + 5 ; funkcja 3: y = 3x + 3

# X = []
# for i in range(-10, 10):
#     X.append(i)

#X = list(range(-10, 10))

X = [i for i in range(-10, 10)]

print(X)

# funkcja 1: y = 5x - 2 ; funkcja 2: y = -2x + 5 ; funkcja 3: y = 3x + 3

# y1 = []
# for i in X:
#     y1.append(5 * i - 2)

Y1 = [5*i - 2 for i in X]
Y2 = [-2*i + 5 for i in X]
Y3 = [ 3*i + 3 for i in X]

plt.axhline() # linia pozioma osi
plt.axvline() # linia pionowa osi
plt.plot(X, Y1, 'ro-')
plt.plot(X,Y2,'b^-')
plt.plot(X,Y3,'gs-')
plt.xlabel("punkty x") # opis osi X
plt.ylabel("wartosci y") # opis osi Y
plt.title("Wykresy funkcji") # tytuł wykresu
plt.show()