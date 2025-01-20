word = input('Задание №1: Введите слово:')
pallindrom = word[::-1]

if(word == pallindrom):
    print('yes')
else:
    print('no')