import time
import math
import pyautogui

# before start
time.sleep(1)



# get screen info
screen_width, screen_height = pyautogui.size()

screen_center = {
    "width": math.floor(screen_width / 2),
    "height": math.floor(screen_height / 2)
}



# do run to front in line direction
def goLineWay():
    pyautogui.moveTo(screen_center["width"] + 200, screen_center["height"] - 200)
    pyautogui.rightClick()
    pyautogui.click()
    print("[LOG]: do goLineWay")




for i in range(6):
    goLineWay()
    time.sleep(0.5)
