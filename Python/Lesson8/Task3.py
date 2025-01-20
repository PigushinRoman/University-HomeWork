# Задание №3

# На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег.
# Одна лодка может выдержать не более m килограмм, при этом в лодку помещается не более 2 человек.
# Определите, какое минимальное число лодок нужно, чтобы перевезти на другой берег всех рыбаков В первую строку вводится число m (1 ≤ m ≤ 10e6) максимальная масса
# которую может выдержать одна лодка. Во вторую строку вводится число n (1 ≤ n ≤ 100) - количество рыбаков.
# В следующие N строк вводится по одному числу Ai (1 ≤ Ai ≤ m) - вес каждого путешественника.
# Программа должна вывести одно число - минимальное количество лодок, необходимое для переправки всех рыбаков на противоположный берег.

#Допустим что N = 10; m = 200; Ai = [60,70,50,66,60,40,60,40,30,30]

n = int(input('Введите N: '))
m = int(input('Введите m: '))
Ai = []

for i in range(0,n,1):
    Ai.append(int(input(f'Введите вес рыбака {i + 1}: ')))

Ai.sort()

start = 0
end = len(Ai) - 1
minimumBoats = 0

while(start <= end):
    if Ai[start] + Ai[end] <= m:
        start+=1
    end -=1
    minimumBoats+=1

print(minimumBoats)






