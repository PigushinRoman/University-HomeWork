import random

def makeList(x): #функция поддержки
    arr = list()
    for i in range(0,x):
        arr.append(random.randrange(1,10,1))
    return arr

def matrixGen(x,y): #функция генерации матрицы где x строки а y столбцы 
    if(x > 0 and y > 0):
        arr = list()
        for i in range(0,y):
            arr.append(makeList(x))
        return arr
    else:
        return 'Не корректный ввод размера. Размер матрицы должен быть больше 0'
        

def matrixSumm(matrixA,matrixB): #функция сложения двух матриц
    matrixC = []
    if(len(matrixA) == len(matrixB) and len(matrixA[0]) == len(matrixB[0])):
        for i in range(0,len(matrixA)):
            matrixC.append(makeList(len(matrixA[0])))
            for j in range(0,len(matrixA[i])):
                matrixC[i][j] = matrixA[i][j] + matrixB[i][j]
        return matrixC
    else:
        return 'Матрицы должны быть одного размера'


matrixA = matrixGen(2,2)
matrixB = matrixGen(2,2)

print(f'Матрица А = {matrixA}')
print(f'Матрица Б = {matrixB}')
print(f'Сумма матриц = {matrixSumm(matrixA,matrixB)}')


