import collections

def get_ageSuffix(petAge):
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
    return ageSpecify

def get_pet(id):
     return pets[id] if id in pets.keys() else False


pets = {
    1:{
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 2,
            "Имя владельца": "Павел"
        },
       },
    2:{
        "Каа": {
            "Вид питомца": "Желторотый питон",
            "Возраст питомца": 1,
            "Имя владельца": "Саша"
        },
       },
}



def update(id,key,value):
    pet = get_pet(id)
    if(pet != False):
        if(key in pet[list(pet.keys())[0]]):
          pet[list(pet.keys())[0]][key] = value
          pets[id] = pet
          return 'Успешно обновлено'
        if(key == 'Имя питомца'):
            pets[id] = {value: pet[list(pet.keys())[0]]}
            return 'Успешно обновлено'
        else:
            return 'Обновление не удалось'
    else:
        return 'Питомец не найден'
         

def create(petName,petSpecie,petAge,petOwner):
    last = collections.deque(pets, maxlen=1)[0] + 1
    pets[last] = {
        petName: {
        "Вид питомца": petSpecie,
        "Возраст питомца": petAge,
        "Имя владельца": petOwner
        }
    }
    return f'Запись успешно добавлена. ID = {last}'

def delete(id):
    pet = get_pet(id)
    if(pet != False):
         del pets[id]
         return 'Запись удалена'
    return 'Запись не найдена'

def read(id):
    pet = get_pet(id)
    return f'{list(pet.values())[0]['Вид питомца']} по кличке {list(pet.keys())[0]}. Возраст питомца: {list(pet.values())[0]['Возраст питомца']} {get_ageSuffix(int(list(pet.values())[0]['Возраст питомца']))}. Имя владельца: {list(pet.values())[0]['Имя владельца']}' if pet != False else 'Питомец не найден'

def show_all_pet():
    for i in pets:
        print(read(i))

def id_input():
    id = int(input('Введите ID питомца(число): '))
    return id

def create_input():
    petName = input('Введите имя питомца: ')
    petSpecie = input('Введите вид питомца: ')
    petAge = int(input('Введите возраст питомца(число): '))
    petOwner = input('Введите имя владельца: ')
    return create(petName,petSpecie,petAge,petOwner)

def update_input(id):
    pet = get_pet(id)
    if(pet != False):
        print('Введите число слева от пункта для выбора параметра что нужно обновить и нажмите Enter:')
        print('1. Имя питомца\n2. Вид питомца\n3. Возраст питомца\n4. Хозяин питомца')
        key = ''
        choise = int(input())
        if(choise == 1):
            key = 'Имя питомца'
            value = input(f'Введите новое значение: ')
            return update(id,key,value)
        if(choise == 2):
            key = 'Вид питомца'
            value = input(f'Введите новое значение: ')
            return update(id,key,value)
        if(choise == 3):
            key = 'Имя питомца'
            value = int(input(f'Введите новое значение(число): '))
            return update(id,key,value)
        if(choise == 4):
            key = 'Имя владельца'
            value = input(f'Введите новое значение: ')
            return update(id,key,value)
    else:
        return 'Питомец не найден'
    

def interface():
    command = ''
    print('Список команд:\ncreate - создать запись\nread - Получить информацию о питомце\nupdate - обновить информацию о питомце\ndelete - удалить информацию\n\nlist - список всех животных\nstop - остановить программу')
    while(command != 'stop'):
        command = input('Введите команду: ')
        if(command == 'create'):
           print(create_input())
        if(command == 'read'):
            print(read(id_input()))
        if(command == 'update'):
            print(update_input(id_input()))
        if(command == 'delete'):
            print(delete(id_input()))
        if(command == 'list'):
            show_all_pet()
    print('Работа завершена')
         
interface()