# 1
def perimeter(a, b, c):
    if a.isdigit() and b.isdigit() and c.isdigit():
        a = int(a)
        b = int(b)
        c = int(c)
        p = a + b + c
        return f'Периметр: {p}'
    else:
        return 'Error! Введите корректное число!'

a = input('Введите значение a: ')
b = input('Введите значение b: ')
c = input('Введите значение c: ')
print(perimeter(a, b, c))



# 2
def ploshad(a, h):
    if a.isdigit() and h.isdigit():
        a = int(a)
        h = int(h)
        s = (a*h) // 2
        return f'Площадь: {s}'
    else:
        return 'Error! Введите корректное число!'

a = input('Введите значение a (сторона, на которую опускается высота): ')
h = input('Введите значение h (высота, которая опускается на сторону a): ')
print(ploshad(a, h))



# 3
from math import *
def poly_perimeter(a, b, c):
    if not a.isdigit() or not b.isdigit() or not c.isdigit():
        return 'Error! Введите корректное число!'
    else:
        a = int(a)
        b = int(b)
        c = int(c)
        poly = (a+b+c) // 2
        return f'Полупериметр: {poly}'

a = input('Введите значение a (первая сторона): ')
b = input('Введите значение b (вторая сторона): ')
c = input('Введите значение c (третья сторона): ')
print(poly_perimeter(a, b, c))



def ploshad_ger(poly, a, b, c):
    if not poly.isdigit() or not a.isdigit() or not b.isdigit() or not c.isdigit():
        return 'Error! Введите корректное число!'
    else:
        poly = int(poly)
        a = int(a)
        b = int(b)
        c = int(c)
        s = isqrt(poly * (poly - a)*(poly - b)*(poly - c))
        return f'Площадь по формуле Герона: {s}'

a = input('Введите значение a (первая сторона): ')
b = input('Введите значение b (вторая сторона): ')
c = input('Введите значение c (третья сторона): ')
poly = input('Введите значение полупериметра: ')
print(ploshad_ger(poly, a, b, c))



# 4
def radius_vpis(s, poly):
    if not s.isdigit() or not poly.isdigit():
        return 'Error! Введите корректное число!'
    else:
        s = int(s)
        poly = int(poly)
        r = s // poly
        return f'Радиус вписанного треугольника: {r}'

s = input('Введите значение s (площадь: ')
poly = input('Введите значение полупериметра: ')
print(radius_vpis(s, poly))



#  5
def radius_opis(a, b, c, s):
    if not a.isdigit() or not b.isdigit() or not c.isdigit() or not s.isdigit():
        return 'Error! Введите корректное число!'
    else:
        a = int(a)
        b = int(b)
        c = int(c)
        s = int(s)
        r = (a*b*c) // (4*s)
        return f'Радиус описанного треугольника: {r}'

a = input('Введите значение a (первая сторона): ')
b = input('Введите значение b (вторая сторона): ')
c = input('Введите значение c (третья сторона): ')
s = input('Введите значение s (площадь: ')
print(radius_opis(a, b, c, s))
