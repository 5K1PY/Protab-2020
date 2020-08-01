import maze
from math import inf
from heapq import *

c = maze.Connect("SK1PY", "mallet")

wall_strength = 20
print(c.width, c.height)
bludiste = c.get_all()
byl_bludiste = [[(False, (None, None), None)]*c.height for i in range(c.width)]  # (was here, from where I got here, with which keystroke)
x, y = c.x(), c.y()

active_nodes = [(0, (x, y), (None, None), None)]  # heap for nodes

while True:
    length, (x, y), (last_x, last_y), com = heappop(active_nodes)

    if byl_bludiste[x][y][0] is True:
        continue  # was here already
    byl_bludiste[x][y] = (True, (last_x, last_y), com)

    if bludiste[x][y] == 3:
        break  # found treasure

    if x + 1 < c.width:
        l1, com = (wall_strength, 'd'*wall_strength) if bludiste[x+1][y] == 2 else (1, 'd')
        if (byl_bludiste[x+1][y][0] is False):
            heappush(active_nodes, (length + l1, (x+1, y), (x, y), com))

    if y + 1 < c.width:
        l1, com = (wall_strength, 's'*wall_strength) if bludiste[x][y+1] == 2 else (1, 's')
        if (byl_bludiste[x][y+1][0] is False):
            heappush(active_nodes, (length + l1, (x, y+1), (x, y), com))

    if x > 0:
        l1, com = (wall_strength, 'a'*wall_strength) if bludiste[x-1][y] == 2 else (1, 'a')
        if (byl_bludiste[x-1][y][0] is False):
            heappush(active_nodes, (length + l1, (x-1, y), (x, y), com))

    if y > 0:
        l1, com = (wall_strength, 'w'*wall_strength) if bludiste[x][y-1] == 2 else (1, 'w')
        if (byl_bludiste[x][y-1][0] is False):
            heappush(active_nodes, (length + l1, (x, y-1), (x, y), com))

commands = []
while True:  # reconstructing solution
    _, (x, y), command = byl_bludiste[x][y]
    if command is None:
        break
    commands.append(command)

commands = ''.join(commands)
commands = commands[::-1]

for command in commands:  # executing solution
    c.move(command)
