# age = int(input('Ile masz lat?   '))
#
# while age < 18:
#     age = int(input('Zły wybór, jeszcze raz:   '))
# print('Wiek zweryfikowany, zapraszamy')

login_list = ['Kamil01', 'AlicjaXD', 'Areczek', 'PaniDominika']

user_login = input('Wpisz login:   ')
while user_login not in login_list:    # sprawdż, czy login nie jest na liście
    print('Niepoprawny login')
    user_login = input('Wpisz login:   ')

print(f'Witaj {user_login}')

