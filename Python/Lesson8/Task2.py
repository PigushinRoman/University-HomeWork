n = int(input('Введи n: '))

array = list(map(int, input('Введи массив чисел через пробел: ').split()))
array = array[0:n]
array = array[-1:] + array[:-1]
print(array)