# 1. Odczyt pliku csv z zapisem poszczegolnych

# with open(r'data\rozliczenie.csv') as file1:
with open('data\\rozliczenie.csv') as file1:
    content = file1.readlines()

print(content)
print(content[7])
print(content[7][5:9])

for i in range(len(content)):
    content[i] = content[i].split(',')
print(content)
print(content[5][3])

# 2. Obliczenie sredniej wyplaty
total = 0
for i in range(1, len(content)):   # omijamy 1wszą linię
#    print(f'Wyplata: {content[i][1]}')
    total += int(content[i][1])
average_salary = total / (len(content)-1)
print(f'średnia wypłata: {round(average_salary, 2)}')

# 3. Obliczenie liczby kobiet na macierzynskim
total = 0
for i in range(1, len(content)):
#     content[i][4] = content[i][4].replace('\n','')
#    print(f'Macierzynski: {content[i][4]}')
    if content[i][4][0].lower() == 't' and content[i][3] == 'k':
        total += 1
print(f'Liczba Pań na macierzyńskim: {total}')

# string.replace('a','')