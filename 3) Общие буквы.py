'''
На вход подаются две строки (раздельные вводы), состоящие из строчных латинских букв без пробелов.
Нужно найти общие буквы, которые встречаются в обеих строках (хотя бы по одному разу). Результат вывести
в виде строки, отсортированной по алфавиту. Если общих букв нет — вывести пустую строку.
Гарантируется, что длина каждой строки не превышает 100 символов.



Пример 1:
Вход:
"hello"
"world"
Выход: "lo" (буквы l и o встречаются в обеих строках)



Пример 2:
Вход:
"abc"
"def"
Выход: "" (пустая строка)
'''



# С примером
f1 = 'abc'.strip().replace(' ', '')
f2 = 'def'.strip().replace(' ', '')

f11 = []
for i in f1:
    f11.append(i)
print(f11)

f22 = []
for i in f2:
    f22.append(i)
print(f22)

d = set()
for elem1 in f11:
    for elem2 in f22:
        if elem1 == elem2:
            d.add(elem1)
d = sorted(d)

r = ''
for i in d:
    r += i
print(r)



# Для пользователя
f1 = input().strip().replace(' ', '')
f2 = input().strip().replace(' ', '')

f11 = []
for i in f1:
    f11.append(i)
print(f11)

f22 = []
for i in f2:
    f22.append(i)
print(f22)

d = set()
for elem1 in f11:
    for elem2 in f22:
        if elem1 == elem2:
            d.add(elem1)
d = sorted(d)

r = ''
for i in d:
    r += i
print(r)