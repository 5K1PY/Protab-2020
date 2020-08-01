import maze


def up():
    if y > 0 and (bludiste[x][y-1] == 0 or bludiste[x][y-1] == 3):
        bludiste[x][y] = 2
        cesta.append((x, y-1))
        prikazy.append('w')
        return True
    return False


def down():
    if y+1 < c.height and (bludiste[x][y+1] == 0 or bludiste[x][y+1] == 3):
        bludiste[x][y] = 2
        cesta.append((x, y+1))
        prikazy.append('s')
        return True
    return False


def left():
    if x > 0 and (bludiste[x-1][y] == 0 or bludiste[x-1][y] == 3):
        bludiste[x][y] = 2
        cesta.append((x-1, y))
        prikazy.append('a')
        return True
    return False


def right():
    if x+1 < c.width and (bludiste[x+1][y] == 0 or bludiste[x+1][y] == 3):
        bludiste[x][y] = 2
        cesta.append((x+1, y))
        prikazy.append('d')
        return True
    return False


def delta(x1, y1, x2, y2):
    """Returns Manhattan distance."""
    return abs(x1-x2) + abs(y1 - y2)


c = maze.Connect("SK1PY", 'vylet')

bludiste = c.get_all()

print(c.width * c.height)
x = c.x()
y = c.y()

start_x = x
start_y = y

cesta = [(x, y)]
prikazy = []
bludiste[x][y] = 2

# finds square with treasure
for poklad_x in range(len(bludiste)):
    if 3 in bludiste[poklad_x]:
        poklad_y = bludiste[poklad_x].index(3)
        break


max_length = 0
best_cesta = []
fncs = [[0, (0, -1), up], [0, (0, 1), down], [0, (-1, 0), left], [0, (1, 0), right]]  # functions for moving in directions
while True:

    # sort order of functions to prioritize moving away from treasure
    for fnc in fncs:
        fnc[0] = delta(poklad_x, poklad_y, x + fnc[1][0], y + fnc[1][1])
    fncs.sort(reverse=True)
    
    # move
    for fnc in fncs:
        moved = fnc[2]()
        if moved is True:
            break

    # can't move anywhere
    if moved is False:
        bludiste[x][y] = 2
        cesta.pop()
        prikazy.pop()
        x, y = cesta[-1]

    print(len(cesta))
    x, y = cesta[-1]
    if bludiste[x][y] == 3:
        break  # found treasure

for p in prikazy:
    c.move(p)
