from utils import randBool, randCell,randNeighbor, randNum
from clouds import Clouds
import os
# 0 - пол
# 1 - дерево
# 2 - река
# 3 - магазин улучшений
# 4 - госпиталь
# 5 - огонь

CELL_TYPES = '🟫🌲🟦🏪🏥🔥'
UPGRADE_COST = 1000
HEALTH_COST = 500
RIVER_COUNT = 3
RIVER_LENGTH = 6
FOREST_DENCITY = 45
MAP_WIDTH = 30
MAP_HEIGTH = 20

class Map:

    def __init__(self,w = MAP_WIDTH,h = MAP_HEIGTH):
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.w = w
        self.h = h
        self.generate_forest(FOREST_DENCITY,100)
        for i in range(0, RIVER_COUNT):
            self.generate_river(RIVER_LENGTH)
        self.generate_shop()
        self.generate_hospital()
        self.clouds = Clouds(w,h)
        self.clouds.update_clouds()

    def check_bounds(self, x, y): # Проверка карты
        if(x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True
    
    def print_map(self,heli): # РЕНДЕР КАРТЫ
        print('⬛' * (self.w + 2))
        for ri in range(self.h):
            print('⬛',end="")
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if(heli.x == ri and heli.y == ci):
                    print("🚁",end="")
                elif(self.clouds.cells[ri][ci] == 1):
                    print("☁️",end=" ")
                elif(self.clouds.cells[ri][ci] == 2):
                    print("🌧️", end=" ")   
                elif(cell >= 0 and cell <len(CELL_TYPES)):
                    print(CELL_TYPES[cell],end="")
            print('⬛')
        print('⬛' * (self.w + 2))
    
    def process_heli(self,heli): # ОБРАБОТЧИК ВЕРТОЛЁТА
        if(self.cells[heli.x][heli.y] == 2):
            heli.tank = heli.maxTank
        if(self.cells[heli.x][heli.y] == 5):
            if(heli.tank > 0):
                self.cells[heli.x][heli.y] = 1
                heli.points += 100
                heli.globalScore += 100
                heli.tank -= 1
        if(self.cells[heli.x][heli.y] == 3):
            if(heli.points >= UPGRADE_COST):
                heli.maxTank += 1
                heli.maxHealth += 10
                heli.health = heli.maxHealth
                heli.points = 0
        if(self.cells[heli.x][heli.y] == 4):
            if(heli.points >= HEALTH_COST and heli.health <= heli.maxHealth):
                heli.health += 1000
                heli.points -= HEALTH_COST
        if(self.clouds.cells[heli.x][heli.y] == 2):
            if(heli.health > 0):
                heli.health -= 1
        if(heli.health <= 0):
            os.system('cls')
            print(f"YOU LOSE, YOUR SCORE: {heli.globalScore}")
            exit(0)
    
    # ГЕНЕРАТОРЫ

    def generate_river(self,l): # РЕКА
        rc = randCell(self.w,self.h)
        rx,ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randNeighbor(rx,ry)
            rx2,ry2 = rc2[0],rc2[1]
            if(self.check_bounds(rx2,ry2)):
                self.cells[rx2][ry2] = 2
                rx,ry = rx2,ry2
            l -= 1

    def generate_forest(self,r,mxr): # ЛЕС
        for ri in range(self.h):
            for ci in range(self.w):
                if randBool(r,mxr):
                    self.cells[ri][ci] = 1
    
    def generate_tree(self): # ДЕРЕВО
        c = randCell(self.w,self.h)
        cx,cy = c[0],c[1]
        if(self.check_bounds(cx,cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1

    def generate_fire(self): # ОГОНЬ
        c = randCell(self.w,self.h)
        cx,cy = c[0],c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5
    
    def update_fire(self,heli): # ОБРАБОТЧИК ОГНЯ
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
                    heli.health -= 1
        for i in range(1,randNum(1,5)):
            self.generate_fire()
    
    def generate_shop(self):
        c = randCell(self.w,self.h)
        cx,cy = c[0],c[1]
        self.cells[cx][cy] = 3
    
    def generate_hospital(self):
        c = randCell(self.w,self.h)
        cx,cy = c[0],c[1]
        self.cells[cx][cy] = 4
    
    def export_data(self):
        return{"cells":self.cells}
    
    def import_data(self,data):
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]
    
    
    

