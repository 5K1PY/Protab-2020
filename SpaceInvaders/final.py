import maze
from math import inf

def my_index(l, x, a=-1):
    if x not in l:
        return a
    else:
        return l.index(x)


c = maze.Connect('SK1PY', 'yyytyy')

x = c.x()
ceiling = 10
while True:
    mapa = c.get_all()

    aliens = [my_index(mapa[i], 1) for i in range(len(mapa))]
    deathly = [my_index(mapa[i], 2) for i in range(len(mapa))]

    direct = aliens.index(max(aliens))

    if x > 0:
        if x < direct:
            if deathly[x-1] >= ceiling or deathly[x-1] >= deathly[x]:
                c.move('a')
                x -= 1

    if x+1 < len(mapa):
        if x > direct:
            if deathly[x+1] >= ceiling or deathly[x+1] >= deathly[x]:
                c.move('d')
                x += 1

    c.move('w')