# 1
def square_sum(a, b):
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        f = a**2 + 2*a*b + b**2
        return f
    else:
        return 'Error! Введите корректное число!'

# a = input('Введите первое значение: ')
# b = input('Введите второе значение: ')
# print(square_sum(a, b))



# 2
def square_minus(a, b):
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        f = a**2 - 2*a*b + b**2
        return f
    else:
        return 'Error! Введите корректное число!'

# a = input('Введите первое значение: ')
# b = input('Введите второе значение: ')
# print(square_minus(a, b))



# 3
def minus_squares(a, b):
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        f = (a-b) * (a+b)
        return f
    else:
        return 'Error! Введите корректное число!'

# a = input('Введите первое значение: ')
# b = input('Введите второе значение: ')
# print(minus_squares(a, b))



# 4
def cube_sum(a, b):
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        f = a**3 + 3*(a**2)*b + 3*a*(b**2) + b**3
        return f
    else:
        return 'Error! Введите корректное число!'

# a = input('Введите первое значение: ')
# b = input('Введите второе значение: ')
# print(cube_sum(a, b))



# 5
def cube_minus(a, b):
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        f = a ** 3 - 3 * (a ** 2) * b + 3 * a * (b ** 2) - b ** 3
        return f
    else:
        return 'Error! Введите корректное число!'

# a = input('Введите первое значение: ')
# b = input('Введите второе значение: ')
# print(cube_minus(a, b))



# 6
def sum_cube(a, b):
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        f = (a + b) * (a**2 - a*b + b**2)
        return f
    else:
        return 'Error! Введите корректное число!'

# a = input('Введите первое значение: ')
# b = input('Введите второе значение: ')
# print(sum_cube(a, b))



# 7
def minus_cube(a, b):
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        f = (a + b) * (a**2 + a*b + b**2)
        return f
    else:
        return 'Error! Введите корректное число!'

# a = input('Введите первое значение: ')
# b = input('Введите второе значение: ')
# print(minus_cube(a, b))



# 8
def sum_three_num(a, b, c):
    if a.isdigit() and b.isdigit() and c.isdigit():
        a = int(a)
        b = int(b)
        c = int(c)
        f = a**2 + b**2 + c**2 + 2*a*b + 2*a*c + 2*b*c
        return f
    else:
        return 'Error! Введите корректное число!'

# a = input('Введите первое значение: ')
# b = input('Введите второе значение: ')
# c = input('Введите третье значение: ')
# print(sum_three_num(a, b, c))