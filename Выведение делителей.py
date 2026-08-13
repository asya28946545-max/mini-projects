while True:
    number = int(input('Введите делимое: '))
    a = []

    for x in range(1, 100000):
        if number % x == 0:
            a.append(str(x))

    res = ', '.join(a)
    result = f'Делитель числа {number}: {res}'

    print(result)