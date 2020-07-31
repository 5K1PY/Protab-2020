import maze

c = maze.Connect("SK1PY", "velociraptor")
field = c.get_all()

isles = [field[i][-1] for i in range(len(field))]
jmps = [(False, False)]*len(field)

for i in range(len(jmps)-4, len(jmps)):
    jmps[i] = (True, False)

current = len(jmps) - 5
while current:
    if isles[current] == 0:
        current -= 1
        continue
    if jmps[current+1][0] is True:
        jmps[current] = (True, False)
    elif jmps[current+4][0] is True:
        jmps[current] = (True, True)
    current -= 1

for j in jmps:
    if j[1] is True:
        c.move("w")
    else:
        c.move("d")
