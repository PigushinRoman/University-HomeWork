from pynput import keyboard
from map import Map
import time
import os
from helicopter import Helicopter
import json

tick = 0
TICK_RATE = 0.06
TREE_UPDATE = 50
FIRE_UPDATE = 100
CLOUD_UPDATE = 300
SPEED_ADJUST = 300


map = Map()
heli = Helicopter()


MOVES = {'w': (-1,0), "d":(0,1),"s":(1,0),"a":(0,-1)}
#F - save
#G - load
def process_key(key):
    global heli, tick, map, tick
    try:
        dir = key.char.lower()
        if(dir in MOVES.keys()):
            heli.move(MOVES[dir][0],MOVES[dir][1])
        elif(dir == 'f'):
            data = {"helicopter": heli.export_data(),"clouds": map.clouds.export_data(),"field":map.export_data(),"tick": tick}
            with open("saveData.json","w") as lvl:
                json.dump(data, lvl)
        elif(dir == 'g'):
            with open("saveData.json","r") as lvl:
                data = json.load(lvl)
                heli.import_data(data["helicopter"])
                tick = data["tick"] or 1
                map.import_data(data["field"])
                map.clouds.import_data(data["clouds"])
        elif(dir == 'c'):
            return False
    except Exception as e: print(e)
    
listener = keyboard.Listener(
    on_release=process_key)
listener.start()


while True:
    os.system('cls')
    map.process_heli(heli)
    heli.print_menu()
    map.print_map(heli)
    tick += 1
    if(tick % TREE_UPDATE == 0):
        map.generate_tree()
    if(tick % FIRE_UPDATE == 0):
        map.update_fire(heli)
    if(tick % SPEED_ADJUST == 0):
        FIRE_UPDATE -= 5
        CLOUD_UPDATE -= 5
    if(tick % CLOUD_UPDATE == 0):
        map.clouds.update_clouds()
    
    time.sleep(TICK_RATE)
