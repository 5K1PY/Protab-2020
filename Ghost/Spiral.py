"""Just exploring the task. Doesn't work."""


import maze

c = maze.Connect("SK1PY", "runda")
x, y = 0, 0

comms = ('w', 'a', 's', 'd')
i = -1

mov = 1
increment = False
while True:
    i = (i + 1) % 4
    comm = comms[i]

    for _ in range(mov):
        c.move(comm)

    if increment is False:
        increment = True
    else:
        mov += 1
        increment = False
        print(mov)
