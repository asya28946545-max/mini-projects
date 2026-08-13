from random import *

def sklonenie_slova(x): # Функция для правильного склонения слова "попытка"
    if x % 10 == 1 and x % 100 != 11:
        return f'Сделана {x} попытка'
    elif 2 <= x % 10 <= 4 and (x % 100 < 10 or x % 100 >= 20):
        return f'Сделано {x} попытки'
    else:
        return f'Сделано {x} попыток'

while True:
    num_AI = randint(1, 100)
    k = 0 # Счётчик кол-ва попыток
    max_count = 5 # Ограничение на кол-во попыток
    game_over = False

    print("--- Новая игра! Загадано число от 1 до 100 ---")

    while not game_over:
        num_you = int(input('Ваше предположение: '))
        k += 1
        count = sklonenie_slova(k)
        ostalos = max_count - k

        if num_you == num_AI:
            print('Молодец! Число угадано! Игра завершена!')
            break

        elif k == max_count:
            print(f'Достигнут максимум попыток! Вы проиграли. Было загадано: {num_AI}')
            break

        if num_you > num_AI:
            print(f'Число большое! {count}, осталось {ostalos}')
        else:
            print(f'Число маленькое! {count}, осталось {ostalos}')

    answer = input('Хотите сыграть ещё раз? (да/нет): ')
    if answer != 'да':
        print('Спасибо за игру! До свидания!')
        break