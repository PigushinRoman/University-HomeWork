def fact(n):
    fact = 1
    if(n == 0):
        return 1
    
    for i in range(1,n+1):
        fact *= i
    return fact

def factList(n):
    arr = []
    if(n == 0):
        arr.append(fact(n))
        return arr
    for i in range(n,0,-1):
        arr.append(fact(i))
    return arr
    
print(factList(int(input('Введите число: '))))