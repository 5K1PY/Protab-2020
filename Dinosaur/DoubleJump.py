def move(con, str):
    for s in str:
        con.move(s)

import maze

c = maze.Connect("SK1PY", "archeopteryx")
field = c.get_all()

isles = [field[i][-1] for i in range(len(field))]
jmps = [(False, 1) for i in range(len(isles))]

for i in range(len(jmps)-4, len(jmps)):
    jmps[i] = (isles[i] == 1, 1)

current = len(jmps) - 4
while current >= 0:
    current -= 1
    if isles[current] == 0:
        continue
    elif jmps[current+1][0] is True:
        jmps[current] = (True, 1)
    elif jmps[current+4][0] is True:
        jmps[current] = (True, 4)
    elif jmps[current+6][0] is True:
        jmps[current] = (True, 6)
    elif jmps[current+8][0] is True:
        jmps[current] = (True, 8)

adress = 0
while True:
    print(adress)
    _, jmp = jmps[adress]
    if jmp == 1:
        move(c, "d")
    elif jmp == 4:
        move(c, "wddd")
    elif jmp == 6:
        move(c, "wwdddd")
    elif jmp == 8:
        move(c, "wdwddddd")
    adress += jmp