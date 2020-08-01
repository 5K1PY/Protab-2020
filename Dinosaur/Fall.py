import maze


def check(x, y, direct):
    """Checks if field has not been searched from."""
    return platforms_result[x][y][direct] is True


c = maze.Connect("SK1PY", "supersaurus")

platforms = c.get_all()
platforms_result = [[[True]*2 for i in range(len(platforms[0]))] for i in range(len(platforms))]

stack = [(c.x(), c.y(), 1, '')]
while True:
    x, y, direct, t = stack[-1]

    platforms_result[x][y][direct] = False

    if platforms[x][y] == 2:  # found cake
        r = t
        break

    elif y + 1 == len(platforms[0]):  # fell too down
        stack.pop()
        continue
    elif platforms[x][y] == 1:  # crashed into wall
        stack.pop()
        continue
    if platforms[x][y+1] != 1:  # falling
        if not (0 <= x + direct and x + direct < len(platforms)) or not check(x+direct, y+1, direct):
            stack.pop()
            continue
        stack.append((x+direct, y+1, direct, t[:] + ('a' if direct == -1 else 'd')))
        continue

    if x+1 < len(platforms):  # going right
        if platforms[x+1][y+1] == 0 and check(x+1, y+1, 1):
            stack.append((x+1, y+1, 1, t[:] + 'd'))
            continue
        elif platforms[x+1][y+1] == 1 and check(x+1, y, 1):
            stack.append((x+1, y, 1, t[:] + 'd'))
            continue

    if x > 0:  # going left
        if platforms[x-1][y+1] == 0 and check(x-1, y+1, -1):
            stack.append((x-1, y+1, -1, t[:] + 'a'))
            continue
        elif platforms[x-1][y+1] == 1 and  check(x-1, y, -1):
            stack.append((x-1, y, -1, t[:] + 'a'))
            continue

    if 0 <= x + direct*4 and x + direct*4 < len(platforms) and check(x + direct*4, y, direct):  # jump
        stack.append((x + direct*4, y, direct, t[:] + 'wwww'))
        continue

    stack.pop()

for i in range(len(r)):
    com = r[i]
    c.move(com)