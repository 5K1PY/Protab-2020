def move(string):
    for s in string:
        c.move(s)


import maze
from pynput.keyboard import Key, Listener

c = maze.Connect('SK1PY', 'sinus')

# 12, 83 bodů
# move('sssddddddadwww')
# while True:
#     print(c.x(), c.y())
#     move('wwwwwwadadssssssad')
#     move('ssssssaaddwwwwwwad')

# 16 bodů
# move('sssdddddddwww')
# while True:
#     print(c.x(), c.y())
#     move('wwwwwwadssssssad')
#     move('ssssssadwwwwww')

# 18 bodů
move('ddsddssddwwdw')

while True:
    print(c.x(), c.y())
    move('dwwwwwwssssss')
    move('sssssswwwwwwa')