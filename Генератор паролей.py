from random import *
l = int(input('Укажите желаемую длину пароля: '))
a = input('Укажите желаемые буквы: ')
b = input('Укажите желаемые цифры: ')
c = input('Укажите желаемые спец. символы: ')
a1 = choice(a)
b1 = choice(b)
c1 = choice(c)
abc = a1 + b1 + c1
if not abc:
    print('Ошибка! Вы не ввели ни одного символа для генерации пароля!')
else:
    password = ''
    for i in range(l):
        password = password + choice(abc)
    print('Итоговый пароль:', password)