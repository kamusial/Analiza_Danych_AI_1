### antywzorzec
products = ['marchew', 'smietana', 'chleb']
quantity = [1, 5, 2]

for i in range(len(products)):
    print(f'kup {products[i]}, w ilości {quantity[i]}')

my_products = {'marchew':1, 'smietana':5, 'chleb':2, 'marchew':3}  # marcew tylko raz
print(my_products)
print(my_products['smietana'])
my_products['kefir'] = 7
my_products['chleb'] = 4
print(my_products)


