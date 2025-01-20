# Задание №1

# Пользователь вводит целое число. Выведите его строку-описание вида "отрицательное четное число", "нулевое число", "положительное нечетное число",
# например, численным описанием числа 190 является строка "положительное четное число". Если число не является четным - выведите сообщение "число не является четным"

###############################################################

number = int(input('Задание №1. Введите целое число: '))
answer = ''

if number == 0:
    answer = 'нулевое число'
else:
    if number > 0:
        answer +='положительное '
    if number < 0:
        answer +='отрицательное '
    if number % 2 == 0:
        answer +='четное число'
    if number % 2 != 0:
        answer +='нечетное число'

print(answer)


###############################################################

# Задание №2

# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».
# Для решения задачи создайте переменную и в неё положите слово с помощью input()
# А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False

###############################################################

#Фидбэк по задаче:
# Я не понял как это можно выполнить используя только то что дали в рамках курса ДО ЭТОЙ ЗАДАЧИ.
# Если я своим решением не выполнил задачу, отправьте, пожалуйста, вариант того как я должен был её сделать, чтобы на будущее было понятно:Я могу использовать только то что дали или нет.


word = input('Задание №2. Введите строку латинницей: ')

if('a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word):
    countA = False
    countE = False
    countI = False
    countO = False
    countU = False
    
    if(word.count('a') > 0):
        countA = word.count('a')
    if(word.count('e') > 0):
        countE = word.count('e')
    if(word.count('i') > 0):
        countI = word.count('i')
    if(word.count('o') > 0):
        countO = word.count('o')
    if(word.count('u') > 0):
        countU = word.count('u')

    consonants = len(word) - sum([countA,countE,countI,countO,countU],0)
    vowels = sum([countA,countE,countI,countO,countU],0)
    
    print(f'Cогласных {consonants}. Гласных {vowels}')
    print(f'a - {countA}\ne - {countE}\ni - {countI}\no - {countO}\nu - {countU}')
    
        
else:
    print(f'В слове: {word} {len(word)} согласных и False гласных')




###############################################################

# Задание №3

# Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали, что минимальная сумма инвестиций - X долларов,
# больше инвестировать можно сколько угодно. У Майкла A долларов, у Ивана B долларов.
# Если оба могут вложиться выведите 2, если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.

###############################################################

Michael,Ivan,MinimalToInvest = map(float,input('\nЗадание №3, введите через пробел: суммаМайкла суммаИвана минимальнаяСуммаДляИнвестирования: ').split())
result = ''

if(Michael < MinimalToInvest and Ivan < MinimalToInvest and Ivan + Michael < MinimalToInvest): #Никто не может
    result = 0

if(Michael < MinimalToInvest and Ivan < MinimalToInvest and Ivan + Michael >= MinimalToInvest): #Могут только вместе
    result = 1

if(Michael >= MinimalToInvest and Ivan >= MinimalToInvest): #Могут оба
    result = 2

else:
    if(Michael >= MinimalToInvest):
        result = 'Mike' #Только Майкл
    if(Ivan >= MinimalToInvest):
        result = 'Ivan' #Только Иван
    
print(result)
###############################################################