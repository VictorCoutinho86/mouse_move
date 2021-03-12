import pyautogui
import random
import time

pyautogui.FAILSAFE = False
while True:
    print("Movendo mouse...")
    pyautogui.moveTo(random.randint(0, 800), random.randint(0,600))
    time.sleep(30)
