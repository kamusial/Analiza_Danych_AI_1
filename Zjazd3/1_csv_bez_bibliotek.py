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


