from random import *

print('--- Загадай число от 1 до 100, а я угадаю! ---')

l = 1
r = 100
k = 0

while True:

    num = randint(l, r)
    use = input(f'Это число {num}? (>, <, =): ')

    if use == '>':
        l = num + 1
        k += 1
    elif use == '<':
        r = num - 1
        k += 1
    else:
        k += 1
        print(f'Я угадал! Это число {num}!')
        print(f'Количество попыток: {k}')

        use2 = input('Хотите сыграть ещё? (да/нет): ').lower()
        if use2 == 'да':
            l = 1
            r = 100
            k = 0
            print(' ')
            print('--- Загадай число от 1 до 100, а я угадаю! ---')
        else:
            print('Спасибо за игру!')
            break