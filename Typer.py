import pyautogui
import time
import datetime
import names
import random

bl = ["Piz-dets", "Svolach", "Suka", "Shlyuha", "Gavno", "Mudak", "Zhopa", "Mandjuk", "Hui", "Blyat"]
string = "Our minds are born festering with sin. Some are so blighted, they will never find redemption. The mind must not be pulled from the roots. My children are without blame, without fault - and without choice. For what is the value of will when the spirit is found wanting?"
listS = string.split()

time.sleep(4)

"""
while datetime.datetime.now().minute != 4:
    pyautogui.write('Ich bin dumm!')
    pyautogui.hotkey('enter')
    time.sleep(0.01)
"""

"""
for x in range(20):
    pyautogui.write("3D-Druckername?")
    pyautogui.hotkey('enter')
    time.sleep(0.1)
"""

for x in listS:
    pyautogui.write(x)
    pyautogui.write(' ')
    time.sleep(0.2)

"""
while True:
    time.sleep(random.randrange(5, 15))
    pyautogui.write("Es ist gerade das Jahr {}, der Monat {}, der Tag {}. Ausserdem ist es gerade {}:{} und {} Sekunden. Millisekunden: {}".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second, datetime.datetime.now().microsecond))
    pyautogui.hotkey('enter')
    #Es ist gerade das Jahr 2021, der Monat 10, der Tag 21. Ausserdem ist es gerade 9:29 und 37 Sekunden. Millisekunden: 311365
"""
