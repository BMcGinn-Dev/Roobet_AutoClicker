# Instructions:
# Set bet amount to .10 cents with $100 to back
# Set mines to 3
# Enter loop of n number for amount of times to play
# Click initial 

#After deeper statistical analysis (simple math), we have discovered the best profit return is 2 square with 4 mines or 4 squares with 2 mines


# These are the squares I am clicking
#    X|X|X|X|X
#    O|O|X|X|X
#    X|X|O|X|X
#    X|X|X|X|X
#    X|X|X|X|X

import time
import pyautogui
from PIL import Image

#Setting the fail-safe --> drag to any corner to kill program or you have to restart computer
pyautogui.FAILSAFE = True

play_btn_coords = (350, 480)
yellow = (255, 235, 59)
green = (76, 175, 80)
wait_yellow = (136, 124, 53)

#Set the number of autoplays you want
autoplays = 100

# Set the amount of seconds you want python to wait before moving to next click
time1 = 2
time2 = 1

play_counter = 0 
win_counter = 0 
loss_counter = 0 

bet_amount = .10
mine_amount = 3

# Method that simply clicks the 3 squares regardless of result
def click3():
    #First Square Move
    pyautogui.click(1000, 400)
    time.sleep(time1)

    #Second Square Move
    pyautogui.click(1100, 400)
    time.sleep(time1)

    #Second Third Move
    pyautogui.click(1200, 500)
    time.sleep(time1)
    
    


def check_color():
    #print("Checking color...")
    # Screenshot the image --> get the color of the pixel
    im = pyautogui.screenshot()
    pixel_color = im.getpixel(play_btn_coords)
    
    if pixel_color == yellow:
        #print("It is yellow")
        return 'Yellow'
    elif pixel_color == green:
        #print("It is green")
        return 'Green'
    else:
        #print("It is neither?")
        return 'Other'
      
      

#Must iniitally click the Play button to start autoplays:    Yellow --> Green
pyautogui.click(350, 480)
time.sleep(2)

#If the color is yellow --> click once, wait, click again, continue loop
#If the collor is green --> click once, continue loop
for i in range(autoplays):
    
    if i > 0 and i % 10 == 0:
        print("Number of successful plays: ", play_counter)
        print("Number of Wins: ", win_counter)
        print("Number of Losses: ", loss_counter)
        print("________")
    
    click3()
    
    color = check_color()
    
    if color == "Yellow":
        #print("Clicking yellow")
        pyautogui.click(350, 480)
        time.sleep(time1)
        play_counter += 1
        loss_counter += 1
        
    elif color == "Green":
        #print("Clicking Green")
        pyautogui.click(350, 480)
        time.sleep(time1)
        pyautogui.click(350, 480)
        time.sleep(time1)
        play_counter += 1
        win_counter += 1
        
    else:
        print("Something went wrong...")
        break
        
    
#Must finally click the Play button to end autoplay:    Green --> Yellow
pyautogui.click(350, 480)
time.sleep(1)
        
print("Number of successful plays: ", play_counter)
print("Number of Wins: ", win_counter)
print("Number of Losses: ", loss_counter) 

