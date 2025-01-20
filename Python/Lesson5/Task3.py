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