import pyautogui
import random
import time

pyautogui.FAILSAFE = False
while True:
    print("Movendo mouse...")
    pyautogui.moveTo(random.randint(799, 800), random.randint(599,600))
    time.sleep(1)
    print("Clicando no local...")
    pyautogui.click()
    time.sleep(30)
