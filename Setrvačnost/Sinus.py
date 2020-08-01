"""Semi-automatic solution for inertia 2 - sinus."""

def move(string):
    """Use to send multiple commands at once."""
    for s in string:
        c.move(s)


import maze
from pynput.keyboard import Key, Listener

c = maze.Connect('SK1PY', 'sinus')

# 12 points
# move('sssddddddadwww')
# while True:
#     print(c.x(), c.y())
#     move('wwwwwwadadssssssad')
#     move('ssssssaaddwwwwwwad')

# 16 points
# move('sssdddddddwww')
# while True:
#     print(c.x(), c.y())
#     move('wwwwwwadssssssad')
#     move('ssssssadwwwwww')

# 18 points
move('ddsddssddwwdw')

while True:
    print(c.x(), c.y())
    move('dwwwwwwssssss')
    move('sssssswwwwwwa')
