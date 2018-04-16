import pyautogui
import time
import sys

# 0.5 sec pause between pyautogui commands
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

# Get resolution of current screen
width, height = pyautogui.size()

# Screen recognition functionality found here:
# http://pyautogui.readthedocs.io/en/latest/screenshot.html#the-locate-functions

def add_instrument(instrument, group):
    # Find instrument group on screen and add new instrument
    if group == 'clearingswitch':
        header_loc = pyautogui.locateCenterOnScreen(r'C:\Users\tdavies\PycharmProjects\untitled\clearingswitch.png')
    elif group == 'ccybasis':
        header_loc = pyautogui.locateCenterOnScreen(r'C:\Users\tdavies\PycharmProjects\untitled\singleccybasis.png')
    elif group == 'sps':
        header_loc = pyautogui.locateCenterOnScreen(r'C:\Users\tdavies\PycharmProjects\untitled\sps.png')

    if header_loc is None:
        return print("Can't find group header - make sure IRODeal is visible")
    else:
        print(header_loc)

    pyautogui.rightClick(header_loc)
    print(pyautogui.locateCenterOnScreen(r'C:\Users\tdavies\PycharmProjects\untitled\add2.png'))
    pyautogui.click(pyautogui.locateCenterOnScreen(r'C:\Users\tdavies\PycharmProjects\untitled\add2.png'))
    pyautogui.typewrite(str(instrument), 0.05)
    time.sleep(1)
    print(pyautogui.locateCenterOnScreen(r'C:\Users\tdavies\PycharmProjects\untitled\ok2.png'))
    pyautogui.click(pyautogui.locateCenterOnScreen(r'C:\Users\tdavies\PycharmProjects\untitled\ok2.png'))


def add_instrument_test(instrument, group):
    print(instrument)
    print(group)

add_instrument(" ".join(sys.argv[1:-1]), "".join(sys.argv[-1:]))