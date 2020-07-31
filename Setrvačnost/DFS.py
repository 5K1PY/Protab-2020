import maze
import collections

c = maze.Connect('SK1PY', 'sinus')
maze = [[[None, {(None, None): tuple([None]*5)}] for j in range(10000)] for i in range(1000)]
x, y = c.x(), c.y()
search = collections.deque([(x, y, (0, 0))])
end = False

counter = 0
while True:
    print(counter)
    counter += 1

    x, y, inertia = search.popleft()
    
    delta = (1, 0)
    keys = ('w', 'a', 's', 'd')
    for i in range(4):
        delta = delta[1], -delta[0]
        dx, dy = inertia[0] + delta[0], inertia[1] + delta[1]
        if x + dx < len(maze) and y + dy < len(maze[0]):
            if maze[x + dx][y + dy][0] is None:
                maze[x + dx][y + dy][0] = c.get(x + dx, y + dy)
            if maze[x + dx][y + dy][0] == 0:
                if (dx, dy) not in maze[x + dx][y + dy][1]:
                    maze[x + dx][y + dy][1][(dx, dy)] = (x, y, inertia[0], inertia[1], keys[i])
                    search.append((x+dx, y+dy, (dx, dy)))
            if maze[x + dx][y + dy][0] == 3:
                maze[x + dx][y + dy][1][(dx, dy)] = (x, y, inertia[0], inertia[1], keys[i])
                end = True
                break

    if end is True:
        break

x, y, i1, i2, key = maze[x + dx][y + dy][1][(dx, dy)]
commands = key
while (i1, i2) in maze[x][y][1]:
    x, y, i1, i2, key = maze[x][y][1][(i1, i2)]
    commands += key

commands = commands[::-1]

for com in commands:
    c.move(com)
