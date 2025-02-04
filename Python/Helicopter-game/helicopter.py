from utils import randCell

MAP_WIDTH = 30
MAP_HEIGTH = 20

class Helicopter:
    def __init__(self,w = MAP_WIDTH,h = MAP_HEIGTH):
        rc = randCell(w,h)
        rx,ry = rc[0],rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.tank = 0
        self.maxTank = 1
        self.points = 0
        self.health = 20
        self.maxHealth = 20
        self.globalScore = 0
    
    def move(self,dx,dy):
        nx = dx + self.x
        ny = dy + self.y
        if(nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx,ny
    def print_menu(self):
        print("🪣 ",self.tank,"/",self.maxTank, " ", "💰 ","/",self.points, " ", "❤️ ","/",self.health)

        
    def export_data(self):
        return {
            "points": self.points,
            "globalScore": self.globalScore,
            "health": self.health,
            "maxHealth": self.maxHealth,
            "x": self.x,"y": self.y,
            "tank": self.tank,
            "mxtank": self.maxTank,
        }
    def import_data(self,data):
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.points = data['points'] or 0
        self.globalScore = data['globalScore'] or 0
        self.health = data["health"] or 20
        self.maxHealth = data["maxHealth"] or 20
        self.tank = data["tank"] or 1
        self.maxTank = data["mxtank"] or 1




