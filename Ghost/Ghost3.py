import maze
import collections

c = maze.Connect("SK1PY", "taktofaktne")

n = 10000
width = 2*n
bludiste = [[None]*width for i in range(width)]
phased_bludiste = [[(-1, None, None)]*width for i in range(width)]  # when i got here, from where, with which keystroke
x, y = c.x() + n, c.y() + n

alive_nodes = [(x, y)]  # searching through walls from these
active_nodes = collections.deque([(x, y)])  # activly searching from
phased_bludiste[x][y] = (0, (0, 0), None)

phased = 0
policek = 0
while True:
    # part for search in empty squares
    while len(active_nodes) > 0:
        print(policek)
        x, y = active_nodes.popleft()
        if x + 1 < width:
            if bludiste[x+1][y] is None:
                bludiste[x+1][y] = c.get(x+1 - n, y - n)
            if (bludiste[x+1][y] == 0 or bludiste[x+1][y] == 3) and (phased_bludiste[x+1][y][0] == -1):
                alive_nodes.append((x+1, y))
                active_nodes.append((x+1, y))
                phased_bludiste[x+1][y] = (phased, (x, y), 'd')
                policek += 1
                if bludiste[x+1][y] == 3:
                    break
        if y + 1 < width:
            if bludiste[x][y+1] is None:
                bludiste[x][y+1] = c.get(x - n, y+1 - n) 
            if (bludiste[x][y+1] == 0 or bludiste[x][y+1] == 3) and (phased_bludiste[x][y+1][0] == -1):
                alive_nodes.append((x, y+1))
                active_nodes.append((x, y+1))
                phased_bludiste[x][y+1] = (phased, (x, y), 's')
                policek += 1
                if bludiste[x][y+1] == 3:
                    break
        if x > 0:
            if bludiste[x-1][y] is None:
                bludiste[x-1][y] = c.get(x-1 - n, y - n) 
            if(bludiste[x-1][y] == 0 or bludiste[x-1][y] == 3) and (phased_bludiste[x-1][y][0] == -1):
                alive_nodes.append((x-1, y))
                active_nodes.append((x-1, y))
                phased_bludiste[x-1][y] = (phased, (x, y), 'a')
                policek += 1
                if bludiste[x-1][y] == 3:
                    break
        if y > 0:
            if bludiste[x][y-1] is None:
                bludiste[x][y-1] = c.get(x - n, y-1 - n) 
            if (bludiste[x][y-1] == 0 or bludiste[x][y-1] == 3) and (phased_bludiste[x][y-1][0] == -1):
                alive_nodes.append((x, y-1))
                active_nodes.append((x, y-1))
                phased_bludiste[x][y-1] = (phased, (x, y), 'w')
                policek += 1
                if bludiste[x][y-1] == 3:
                    break

    if len(active_nodes) > 0:
        break  # found treasure

    # part for search through walls
    phased += 1
    new_alive_nodes = []
    for node in alive_nodes:
        x, y = node
        if x + 1 < width and (phased_bludiste[x+1][y][0] == -1):
            new_alive_nodes.append((x+1, y))
            active_nodes.append((x+1, y))
            phased_bludiste[x+1][y] = (phased, (x, y), 'd')
            policek += 1
        if y + 1 < width and (phased_bludiste[x][y+1][0] == -1):
            new_alive_nodes.append((x, y+1))
            active_nodes.append((x, y+1))
            phased_bludiste[x][y+1] = (phased, (x, y), 's')
            policek += 1
        if x > 0 and (phased_bludiste[x-1][y][0] == -1):
            new_alive_nodes.append((x-1, y))
            active_nodes.append((x-1, y))
            phased_bludiste[x-1][y] = (phased, (x, y), 'a')
            policek += 1
        if y > 0 and (phased_bludiste[x][y-1][0] == -1):
            new_alive_nodes.append((x, y-1))
            active_nodes.append((x, y-1))
            phased_bludiste[x][y-1] = (phased, (x, y), 'w')
            policek += 1

    alive_nodes = new_alive_nodes
    active_nodes = collections.deque(alive_nodes)

x, y = active_nodes[-1]
commands = []
while True:  # reconstructing solution
    _, (x, y), command = phased_bludiste[x][y]
    if command is None:
        break
    commands.append(command)
commands.reverse()

for command in commands:  # executing solution
    c.move(command)
