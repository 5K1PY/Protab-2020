"""Just exploring the task. Doesn't work."""


import maze
from math import inf

c = maze.Connect('SK1PY', 'lebkoun')

x = c.x()
go = x
while True:
    mapa = c.get_all()
    is_aliens = [1 in mapa[i] for i in range(len(mapa))]
    # print(x, is_aliens[x], 2 in mapa[x])
    if 2 in mapa[x]:
        if x > 0:
            c.move('a')
            x -= 1
        elif x < len(mapa):
            c.move('d')
            x += 1
    
    elif 1 not in mapa[x]:
        dx = 1
        while True:
            if x + dx < len(mapa) and is_aliens[x+dx] and 2 not in mapa[x+1]:
                c.move('d')
                x += 1
                break
            if 0 < x - dx and is_aliens[x-dx] and 2 not in mapa[x-1]:
                c.move('a')
                x -= 1
                break
            dx += 1
    
    c.move('w')