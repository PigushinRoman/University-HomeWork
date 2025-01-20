number = int(input('Задание №1. Введите целое число: '))
answer = ''

if number == 0:
    answer = 'нулевое число'
else:
    if number > 0:
        answer +='положительное '
    if number < 0:
        answer +='отрицательное '
    if number % 2 == 0:
        answer +='четное число'
    if number % 2 != 0:
        answer +='нечетное число'

print(answer)