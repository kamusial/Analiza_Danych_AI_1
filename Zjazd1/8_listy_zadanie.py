customer_name_list = ['Kamil', 'Basia', 'Kasia', 'Patryk', 'Kuba']

for i in range(len(customer_name_list)):
    if customer_name_list[i][-1] == 'a':
        print(f'Witam Panią {customer_name_list[i]}')
    else:
        print(f'Witam Pana {customer_name_list[i]}')

for name in customer_name_list:
    if name[-1] == 'a':
        print(f'Witam Panią {name}')
    else:
        print(f'Witam Pana {name}')