my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 1. Передать в функцию итератор
# 2. Проверить, выполняются ли условия выхода из рекурсии, если да - вывести "Конец списка" и прекратить выполнение, если нет, переход к п.3
# 3. Вывести элемент массива с индексом равным итератору
# 4. Заново вызвать функцию с итератор + 1

def recursion(iterator = 0):
    if(iterator == len(my_list)):
        return 'Конец списка'
    print(my_list[iterator])
    return recursion(iterator + 1)

recursion()