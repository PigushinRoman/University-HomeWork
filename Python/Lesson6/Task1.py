n = int(input('Задание №1: Введите N:'))
tempN = n
nullNumCounter = 0

while(tempN > 0):
    number = int(input('Введите целое число: '))
    if(number == 0):
        nullNumCounter += 1
    tempN -= 1
    
print(f'Введено {n} чисел из них {nullNumCounter} нули')