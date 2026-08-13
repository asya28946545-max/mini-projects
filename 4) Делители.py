'''
На вход подаётся натуральное число N (1 ≤ N ≤ 10^6). Нужно найти его наименьший простой делитель.
Если число простое — вывести само число.



Пример:
Вход: 15
Выход: 3
'''


def p(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return x > 1

def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for N in range(1, 10**6):
    d = [i for i in div(N) if p(i)]
    if len(d) > 0:
        if N == 1:
            print(1)
        else:
            print(min(d))