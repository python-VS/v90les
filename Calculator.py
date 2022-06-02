# Калькулятор Сахарова
number_1 = float(input('введите 1е число: '))
symbol = input('Введите тип операции (символ): ')
number_2 = float(input('Введите 2е число: '))

if symbol == '+':
    result = number_1 + number_2
    print('Результат: ' + str(result))
elif symbol == '-':
    result = number_1 - number_2
    print('Результат: ' + str(result))
elif symbol == '/':
    result = number_1 / number_2
    print('Результат: ' + str(result))
elif symbol == '*':
    result = number_1 * number_2
    print('Результат: ' + str(result))
elif symbol == '**':
    result = number_1 ** number_2
    print('Результат: ' + str(result))
elif symbol == '%':
    result = number_1 % number_2
    print('Результат: ' + str(result))
elif symbol == '//':
    result = number_1 // number_2
    print('Результат: ' + str(result))
else:
    print('Невозможно выполнить операцию!')
