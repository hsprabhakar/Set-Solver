import time
import win32api, win32con

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.005)
    print('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.005)
    print('left release')

def mousePos(cord):
    win32api.SetCursorPos((cord[0], cord[1]))
     
def get_cords():
    x,y = win32api.GetCursorPos()
    print(x,y)

class Cord:



    x1 = (1068, 433)
    x2 = (899, 437)
    x3 = (734, 436)
    x4 = (574, 427)
    x5 = (418, 438)


    x6 = (1060, 645)
    x7 = (896, 648)
    x8 = (739, 645)
    x9 = (572, 652)
    x10 = (415, 644)

    x11 = (1059, 865)
    x12 = (899, 859)
    x13 = (733, 865)
    x14 = (580, 857)
    x15 = (415, 859)


    ##############################

"""
    x1 = (418, 438)
    x2 = (574, 427)
    x3 = (734, 436)
    x4 = (899, 437)
    
    x5 = (415, 644)
    x6 = (572, 652)
    x7 = (739, 645)
    x8 = (896, 648)
    
    x9 = (415, 859)
    x10 = (580, 857)
    x11 = (733, 865)
    x12 = (899, 859)

    x13 = (1068, 433)
    x14 = (1060, 645)
    x15 = (1059, 865)
"""

def ClickAllComb():
    #click all combinations of cards

    mousePos((418, 438))
    leftClick()
    time.sleep(0.005)

    mousePos((574, 427))
    leftClick()
    time.sleep(0.005)

    mousePos((734, 436))
    leftClick()
    time.sleep(0.005)

"""
    x1 = (418, 438)
    x2 = (574, 427)
    x3 = (734, 436)
    x4 = (899, 437)
    x5 = (415, 644)
    x6 = (572, 652)
    x7 = (739, 645)
    x8 = (896, 648)
    x9 = (415, 859)
    x10 = (580, 857)
    x11 = (733, 865)
    x12 = (899, 859)
    
    x13 = (1068, 433)
    x14 = (1060, 645)
    x15 = (1059, 865)
"""

card_1 = 0
card_2 = 1
card_3 = 2
CARDS = [Cord.x1, Cord.x2, Cord.x3, Cord.x4, Cord.x5, Cord.x6, Cord.x7, Cord.x8, Cord.x9, Cord.x10, Cord.x11, Cord.x12, Cord.x13, Cord.x14, Cord.x15]
length_of_cards = len(CARDS)

finished = False
while not finished:

    mousePos(CARDS[card_1])
    leftClick()
    time.sleep(0.005)
 
    mousePos(CARDS[card_2])
    leftClick()
    time.sleep(0.005)
 
    mousePos(CARDS[card_3])
    leftClick()
    time.sleep(0.005)

    # Iterate Cards 2 and 3
    if card_3 < length_of_cards - 1:
        card_3 += 1
    elif card_3 == length_of_cards - 1:
        card_2 += 1
        card_3 = card_2 + 1

    # Iterate Card 1
    if card_2 == length_of_cards - 2 and card_3 == length_of_cards - 1:
        card_1 += 1
        card_2 = card_1 + 1
        card_3 = card_2 + 1

    if card_1 == length_of_cards - 3 and card_2 == length_of_cards - 1 and card_3 == length_of_cards:
        print("AHAHAHA IT WORKS")
        finished = True
