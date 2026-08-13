def calculator():
    num1 = float(input('Первое число: '))
    operator = input('Оператор (+, -, *, /): ')
    num2 = float(input('Второе число: '))

    if operator == '+':
        return num1 + num2

    elif operator == '-':
        return num1 - num2

    elif operator == '*':
        return num1 * num2

    elif operator == '/':
        return num1 / num2

    else:
        return 'Error'

print(calculator())