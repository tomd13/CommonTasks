import pyautogui

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True

# Get resolution of current screen
width, height = pyautogui.size()

# Screen recognition functionality found here:
# http://pyautogui.readthedocs.io/en/latest/screenshot.html#the-locate-functions

def add_instrument(instrument, group):
    # Find instrument group on screen and add new instrument
    pyautogui.rightClick(pyautogui.locateCenterOnScreen(r'C:\Users\Tom\PycharmProjects\CommonTasks\asiahubjpy.png'))
    pyautogui.typewrite('a')
    pyautogui.press('enter')
    pyautogui.typewrite(str(instrument))
    pyautogui.press('enter', 2, 0.2)

add_instrument('3mL 22-Dec', '')