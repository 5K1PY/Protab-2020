import maze
import collections

c = maze.Connect("SK1PY", "nejbliz")

print(c.width, c.height)
bludiste = c.get_all()
phased_bludiste = [[(-1, None, None)]*c.height for i in range(c.width)]
x, y = c.x(), c.y()

alive_nodes = [(x, y)]
active_nodes = collections.deque([(x, y)])
phased_bludiste[x][y] = (0, (0, 0), None)

print(c.width, c.height)
phased = 0
policek = 0
while True:
    while len(active_nodes) > 0:
        print(policek)
        x, y = active_nodes.popleft()

        if x + 1 < c.width and (bludiste[x+1][y] == 0 or bludiste[x+1][y] == 3) and (phased_bludiste[x+1][y][0] == -1):
            alive_nodes.append((x+1, y))
            active_nodes.append((x+1, y))
            phased_bludiste[x+1][y] = (phased, (x, y), 'd')
            policek += 1
            if bludiste[x+1][y] == 3:
                break
        if y + 1 < c.width and (bludiste[x][y+1] == 0 or bludiste[x][y+1] == 3) and (phased_bludiste[x][y+1][0] == -1):
            alive_nodes.append((x, y+1))
            active_nodes.append((x, y+1))
            phased_bludiste[x][y+1] = (phased, (x, y), 's')
            policek += 1
            if bludiste[x][y+1] == 3:
                break
        if x > 0 and (bludiste[x-1][y] == 0 or bludiste[x-1][y] == 3) and (phased_bludiste[x-1][y][0] == -1):
            alive_nodes.append((x-1, y))
            active_nodes.append((x-1, y))
            phased_bludiste[x-1][y] = (phased, (x, y), 'a')
            policek += 1
            if bludiste[x-1][y] == 3:
                break
        if y > 0 and (bludiste[x][y-1] == 0 or bludiste[x][y-1] == 3) and (phased_bludiste[x][y-1][0] == -1):
            alive_nodes.append((x, y-1))
            active_nodes.append((x, y-1))
            phased_bludiste[x][y-1] = (phased, (x, y), 'w')
            policek += 1
            if bludiste[x][y-1] == 3:
                break

    if len(active_nodes) > 0:
        break

    phased += 1
    new_alive_nodes = []
    for node in alive_nodes:
        x, y = node
        if x + 1 < c.width and (phased_bludiste[x+1][y][0] == -1):
            new_alive_nodes.append((x+1, y))
            active_nodes.append((x+1, y))
            phased_bludiste[x+1][y] = (phased, (x, y), 'd')
            policek += 1
        if y + 1 < c.width and (phased_bludiste[x][y+1][0] == -1):
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
while True:
    _, (x, y), command = phased_bludiste[x][y]
    if command is None:
        break
    commands.append(command)
commands.reverse()

for command in commands:
    c.move(command)