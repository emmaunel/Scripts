import os
import time
import datetime
import webbrowser

from colorama import init
from colorama import Fore

init()

evanescense = 'https://www.youtube.com/watch?v=96MiYk9VYvc'

clear = lambda: os.system('clear')

clear()
print("If you play 'Bring Me To Life' by Evanescence at exactly 11:59:08 on New Years Eve, the first WAKE ME UP will "
      "play exactly at midnight. Start your New Year off right.")

while True:
    nowtime = datetime.datetime.now()
    if nowtime.hour == 23 and nowtime.minute == 59 and nowtime.second == 7:
        print("Playing 'Bring Me To Life")
        webbrowser.open(evanescense)
        break

for x in range(53):
    print(f"Time until New Years: {53 - x} seconds")
    time.sleep(1)


clear()

while True:
    for color in (Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA):
        print(color + "Happy New Year !")
        time.sleep(.03)