x = int(input('Задание №2: Введите целое число: '))
naturalDividerCounter = 0

for i in range(1, x + 1):
    if(x % i == 0):
        naturalDividerCounter+= 1

print(naturalDividerCounter)