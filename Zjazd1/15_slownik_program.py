# program przechowuje i aktualizuje dane o śrendnich ocenach studentów

average_grades = {5234: 4.3, 6454: 3.2, 1234: 5.0}

while True:
    answer = input('Czy chcesz zaktualizować baze?   t/n: ')
    if answer == 't':
        indeks_number = int(input('Podaj numer indeksu:  '))
        average_grade = float(input('Podaj srednia:  '))
        average_grades[indeks_number] = average_grade
        # print
        print(f'W slowniku jest {len(average_grades)} ludzi')
    else:
        break

print('Dalsza część programu')