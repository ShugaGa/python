print('Придумайте пароль.')
while True:
    p1 = input('Введите пароль: ')
    p2 = input('Повторите пароль: ')

    if p1 == p2:
        print('Пароль готов.')
        break
    else:
        print('Пароли не совпадают.')