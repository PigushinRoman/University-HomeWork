petName = input('Введите имя питомца: ')
petSpecie = input('Введите вид питомца: ')
petAge = int(input('Введите возраст питомца: '))
             
ageSpecify = ""
if(petAge >= 5 and petAge <= 20):
        ageSpecify = 'лет'
else:
    if(petAge % 10 == 1):
        ageSpecify = 'год'
    else:
        if(petAge % 10 == 2 or petAge % 10 == 3 or petAge % 10 == 4):
            ageSpecify = 'года'
        else:
              ageSpecify = 'лет'


petOwner = input('Введите имя владельца питомца: ')

pets = dict()
pets[petName] = {
    "Вид питомца": petSpecie,
    "Возраст питомца": f'{petAge} {ageSpecify}',
    "Имя владельца": petOwner
}

print(f'Это {list(pets.values())[0]['Вид питомца']} по кличке {list(pets.keys())[0]}. Возраст питомца: {list(pets.values())[0]['Возраст питомца']}. Имя владельца: {list(pets.values())[0]['Имя владельца']}')



