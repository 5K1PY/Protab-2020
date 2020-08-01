"""Sends keys pressed on keyboard."""

import maze
from pynput.keyboard import Key, Listener

c = maze.Connect('SK1PY', 'emzak')
print(c.width, c.height)

def on_press(key):
    print(key.char)
    if not c.move(key.char):
       print(c.error)
    print(c.x(), c.y())

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
# 