import math
# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход

# у этого класс есть методы:

# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции

class turtle(object):
    def __init__(self,x,y,squarePerMove):
        self.x = x
        self.y = y
        self.squarePerMove = squarePerMove
    def go_up(self):
        self.y += self.squarePerMove
    def go_down(self):
        self.y -= self.squarePerMove
    def go_left(self):
        self.x -= self.squarePerMove
    def go_rigth(self):
        self.x += self.squarePerMove
    def evolve(self):
        self.squarePerMove += 1
    def degrade(self):
        if(self.squarePerMove - 1 <= 0):
            return 'Ошибка. Кол-во клеток должно быть больше 0'
        else:
            self.squarePerMove -= 1
    def count_moves(self,x2,y2):
        distanceX = x2 - self.x
        distanceY = y2 - self.y
        turnCount = int(math.ceil(distanceX + distanceY / self.squarePerMove))
        if(distanceX != distanceY):
            return f'{turnCount} ходов'
        if(distanceX == distanceY):
            return f'{int(turnCount / 2)} ходов'


player = turtle(0,0,1)

print(player.count_moves(6,6))
print(player.count_moves(6,5))
