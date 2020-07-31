def move(string):
    for s in string:
        c.move(s)
        print(c.get(c.x(), c.y()))


import maze
from pynput.keyboard import Key, Listener

c = maze.Connect('SK1PY', 'runda')
print(c.width, c.height)

n = 400
move('w'*(n//2))
move('d'*(n//2))
move('s'*n)
move('a'*n)
move('w'*n)
move('d'*(n//2))

while True:
    move('w')