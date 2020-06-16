import time
import win32api, win32con


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.010)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print("Click.")


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.010)
    print('left Down')


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.010)
    print('left release')


def mousePos(cord):
    win32api.SetCursorPos((cord[0], cord[1]))


def get_cords():
    x, y = win32api.GetCursorPos()
    print(x, y)


class Cord:
    x1 = (618, 276)
    x2 = (771, 276)
    x3 = (830, 276)
    x4 = (939, 276)
    x5 = (618, 418)
    x6 = (721, 418)
    x7 = (834, 418)
    x8 = (939, 418)
    x9 = (618, 559)
    x10 = (721, 559)
    x11 = (834, 559)
    x12 = (938, 559)


def ClickAllComb():
    # click all combinations of cards

    mousePos((618, 276))
    leftClick()
    time.sleep(0.005)

    mousePos((771, 276))
    leftClick()
    time.sleep(0.005)

    mousePos((830, 276))
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
"""

card_1 = 0
card_2 = 1
card_3 = 2
CARDS = [Cord.x1, Cord.x2, Cord.x3, Cord.x4, Cord.x5, Cord.x6, Cord.x7, Cord.x8, Cord.x9, Cord.x10, Cord.x11, Cord.x12]
length_of_cards = len(CARDS)

finished = False
while not finished:

    mousePos(CARDS[card_1])
    leftClick()
    time.sleep(0.010)

    mousePos(CARDS[card_2])
    leftClick()
    time.sleep(0.010)

    mousePos(CARDS[card_3])
    leftClick()
    time.sleep(0.010)

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
