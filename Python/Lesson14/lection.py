from functools import lru_cache # Пока игрался с рекурсией заметил что при итеративном методе дальше 40 программа просто виснет. Загугил, нашёл эту библиотеку. Программа стала работать и при больших значениях
@lru_cache()

def fib(n):
    if(n <= 0):
        return 0
    if(n == 1):
        return 1
    
    return fib(n - 1) + fib(n - 2)

print(fib(256))
