import os
import random
import time

import pyautogui

pyautogui.FAILSAFE = False
posicao = pyautogui.position()

try:
    while True:
        if posicao == pyautogui.position():
            print("Movendo mouse...")
            pyautogui.moveTo(random.randint(799, 800),
                             random.randint(599, 600))
            print("Clicando no local...")
            pyautogui.click()
        print("Atualizando posição do mouse...")
        posicao = pyautogui.position()
        time.sleep(os.getenv("TIMER", 90))
except KeyboardInterrupt:
    print("Parando execução...")
