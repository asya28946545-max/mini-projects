from math import *
def discriminant(a, b, c):
    if a == '0':
        return None
    else:
        a = int(a)
        b = int(b)
        c = int(c)
        D = b**2 - 4*a*c
        if D == 0:
            x = -b / (2*a)
            if x <= -1:
                x = abs(x)
                return f'(x+{x})**2'
            else:
                return f'(x-{x})**2'
        elif D < 0:
            return 'Корней нет'
        else:
            d = isqrt(D)
            x1 = int((-b+d) / (2*a))
            x2 = int((-b-d) / (2*a))
            if a == 1:
                if x1 <= -1 and x2 >= 1:
                    x1 = abs(x1)
                    return f'(x+{x1})(x-{x2})'
                elif x2 <= -1 and x1 >= 1:
                    x2 = abs(x2)
                    return f'(x-{x1})(x+{x2})'
                elif x1 <= -1 and x2 <= -1:
                    x1 = abs(x1)
                    x2 = abs(x2)
                    return f'(x+{x1})(x+{x2})'
                else: # x1 >= 1 and x2 >= 1
                    return f'(x-{x1})(x-{x2})'

            elif a == -1:
                if x1 <= -1 and x2 >= 1:
                    x1 = abs(x1)
                    return f'-(x+{x1})(x-{x2})'
                elif x2 <= -1 and x1 >= 1:
                    x2 = abs(x2)
                    return f'-(x-{x1})(x+{x2})'
                elif x1 <= -1 and x2 <= -1:
                    x1 = abs(x1)
                    x2 = abs(x2)
                    return f'-(x+{x1})(x+{x2})'
                else: # x1 >= 1 and x2 >= 1
                    return f'-(x-{x1})(x-{x2})'

            else:
                if x1 <= -1 and x2 >= 1:
                    x1 = abs(x1)
                    return f'{a}(x+{x1})(x-{x2})'
                elif x2 <= -1 and x1 >= 1:
                    x2 = abs(x2)
                    return f'{a}(x-{x1})(x+{x2})'
                elif x1 <= -1 and x2 <= -1:
                    x1 = abs(x1)
                    x2 = abs(x2)
                    return f'{a}(x+{x1})(x+{x2})'
                else: # x1 >= 1 and x2 >= 1
                    return f'{a}(x-{x1})(x-{x2})'

a = input('Введите первое значение: ')
b = input('Введите второе значение: ')
c = input('Введите третье значение: ')
print(discriminant(a, b, c))