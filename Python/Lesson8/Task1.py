n = int(input())
array = []
for i in range(0,n,1):
    array.append(int(input()))

print(f'{n} чисел - {array[::-1]}')