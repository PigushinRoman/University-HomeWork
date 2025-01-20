A,B = map(int,input('Задание №3: Введите числа А и B через пробел: ').split())

for i in range(A, B+1, 1):
    if(i % 2 == 0):
        print(i)
