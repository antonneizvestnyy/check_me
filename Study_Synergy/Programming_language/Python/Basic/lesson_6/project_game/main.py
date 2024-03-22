from pynput import keyboard
from clouds import Clouds
from map import Map
import time
import os
import json
from helicopter import Helicopter as Heli




TICK_SLEEP = 0.05
TREE_UPDATE = 50
CLOUDS_UPDATE = 100
FIRE_UPDATE = 75
MAP_W, MAP_H = 20, 10

tmp = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helico = Heli(MAP_W, MAP_H)
tick = 1


MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
# q - сохранение , e - восстановление из файла
def work_key(key):
    global helico, tick, clouds, tmp
    c = key.char.lower()
    # обработка движений вертолетика 
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    # сохранение игры
    elif c == 'q': 
        data = {'helicopter': helico.export_data(), #хранение данных
                'clouds': clouds.export_data(),
                'tmp': tmp.export_data(),
                'tick': tick}
        with open('level.json', 'w') as lvl: # with - удобнее работать с файлом
            json.dump(data, lvl)
    # восстановление игры
    elif c == 'e':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            helico.import_data(data['helicopter'])
            tick = data['tick'] or 1
            tmp.import_data(data['tmp'])
            clouds.import_data(data['clouds'])


listener = keyboard.Listener(
        on_press=None,
        on_release=work_key,)
listener.start()



while True:
    os.system('clear') #cls - windows
    tmp.proc_heli(helico, clouds)
    helico.print_stats()
    tmp.print_map(helico, clouds)
    print('tick', tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        tmp.gen_tree()
    if (tick % FIRE_UPDATE == 0):
        tmp.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()

