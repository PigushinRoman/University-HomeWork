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