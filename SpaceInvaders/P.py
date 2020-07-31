import maze

c = maze.Connect('SK1PY', 'lebkoun')

x = c.x()
direct = False
k = 15
while True:
    mapa = c.get_all()
    if 2 in mapa[x]:
        if (direct is True and (2 not in mapa[x+1] or (mapa[x+1].index(2) > mapa[x].index(2)))):
            c.move('d')
            x += 1
            if x + 1 == len(mapa):
                direct = False
        elif (direct is False and (2 not in mapa[x-1] or (mapa[x-1].index(2) > mapa[x].index(2)))):
            c.move('a')
            x -= 1
            if x == 0:
                direct = True
        elif (2 in mapa[x][-k:] and 2 in mapa[x+1][-k:]):
            c.move('a')
            x -= 1
        elif (2 in mapa[x][-k:] and 2 in mapa[x-1][-k:]):
            c.move('d')
            x += 1
    else:
        if (direct is True and (2 not in mapa[x+1] or (mapa[x+1][::-1].index(2) > k))):
            c.move('d')
            x += 1
            if x + 1 == len(mapa):
                direct = False
        if (direct is False and (2 not in mapa[x-1] or (mapa[x-1][::-1].index(2) > k))):
            c.move('a')
            x -= 1
            if x == 0:
                direct = True
    c.move('w')