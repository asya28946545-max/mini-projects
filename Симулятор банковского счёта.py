balance = 0 # Стартовый капитал
history = [] # Список записей о транзанкциях

while True:

    print('''Выберите действие:
    1 - Пополнить баланс
    2 - Снять наличные
    3 - Посмотреть историю операций
    4 - Выход''')

    num_use = input('')

    if not num_use.isdigit():
        print('Ошибка! Введите номер пункта меню от 1 до 4')
        continue
    else:
        num = int(num_use)

    if num == 1:
        num1 = input('Введите сумму: ')

        if not num1.isdigit():
            print('Ошибка! Пожалуйста, введите корректное число!')
        else:
            balance += int(num1)
            history.append(f'Пополнение: +{num1} руб.')
            continue


    elif num == 2:
        num2 = input('Введите сумму: ')

        if not num2.isdigit():
            print('Ошибка! Пожалуйста, введите корректное число!')
        elif int(num2) > balance:
            print('Ошибка! Нельзя снять сумму больше, чем есть на счету!')
        else:
            balance -= int(num2)
            history.append(f'Снятие: -{num2} руб.')
            continue

    elif num == 3:
        print('--- Ваша история операций ---')
        if len(history) == 0:
            print('История пуста')
            continue
        else:
            for i in history:
                print(i)

    else:
        break