import pyautogui

pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

# Get resolution of current screen
width, height = pyautogui.size()

# Screen recognition functionality found here:
# http://pyautogui.readthedocs.io/en/latest/screenshot.html#the-locate-functions

def add_instrument(instrument, group):
    #pyautogui.rightClick(pyautogui.locateCenterOnScreen(r'C:\Users\Tom\PycharmProjects\CommonTasks\Test2.png'))
    pyautogui.click(50, 400)
    pyautogui.click(50, 400)
    pyautogui.typewrite('a')
    pyautogui.press('enter')
    pyautogui.typewrite(str(instrument))
    pyautogui.press('enter', 2, 0.2)

add_instrument('3mL 22-Dec', '')

pyautogui.locateCenterOnScreen(r'C:\Users\Tom\PycharmProjects\CommonTasks\Test2.png')
#pyautogui.typewrite(['a', 'b', 'enter', 'left', 'X', 'Y'])
