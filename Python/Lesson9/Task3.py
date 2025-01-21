# Во входную строку водится последовательность чисел через пробел. 
# Для каждого числа выведите слово ”YES” (в отдельной строке), если это число ранее встречалось в последовательности 
# или ”NO”, если не встречалось.

list = list(map(int,input('Введите последовательность чисел: ').split()))
answer = set()
for i in range(0,len(list)):
    if(list[i] in answer):
        
        print(f'{list[i]} - YES')
    else:
        answer.add(list[i])
        print(f'{list[i]} - NO')