import time
import pyautogui
from PIL import Image

#Setting the fail-safe --> drag to any corner to kill program or you have to restart computer
pyautogui.FAILSAFE = True

play_amount = 500

successful_plays = 0

#play btn coords
play_bttn = (950, 600)

for i in range(play_amount):
    
    if i > 0 and i % 10 == 0:
        print("Number of successful plays: ", successful_plays)
        print("________")
    
    
    pyautogui.click(play_bttn)
    successful_plays += 1
    time.sleep(1)

print("Successful plays: ", successful_plays)
