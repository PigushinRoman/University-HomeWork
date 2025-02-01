# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:

# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

class Cassa(object):
    def __init__(self,sum):
        self.currentSum = sum

    def top_up(self,x):
        self.currentSum += x
        return f'Успешно, итого в кассе: {self.currentSum} руб'

    def count_1000(self):
        result = self.currentSum // 1000
        return result if result >= 1 else 'Тысяч нет'
    
    def take_away(self,x):
        if(self.currentSum - x >= 0):
            self.currentSum -= x
            return f'Успешно, в кассе осталось {self.currentSum} руб'
        else:
            return 'Ошибка, недостаточно средств'


cassa = Cassa(22950)

print(f'В кассе: {cassa.currentSum} руб')
print(f'Целых тысяч - {cassa.count_1000()}')
print(f'{cassa.take_away(22931)}')
print(f'{cassa.take_away(22931)}')
print(f'{cassa.top_up(500)}')
    
    