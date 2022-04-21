import pyautogui
from random import choice
from time import sleep
import _thread

# Nubmer Variable
numbers = '1234567890'
# lower case
lower = 'abcdefghijklmnopqrstuvwxyz'
# upper case
upper = lower.upper();
# other
other = '!"§$%&/()=?.,-_:;'
all = numbers + lower + upper + other


def doitLOL():
    while True:
        pyautogui.write(choice(all));


sleep(4)

try:
    _thread.start_new_thread(doitLOL())
    _thread.start_new_thread(doitLOL())
    _thread.start_new_thread(doitLOL())
    _thread.start_new_thread(doitLOL())
except:
   print("Error: unable to start thread")
