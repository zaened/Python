import pyautogui

# Unten links
x1 = 584
y1 = 474

# Spitze
x2 = 731
y2 = 269

# Unten rechts
x3 = 878
y3 = 474

# Oben links
x4 = 584
y4 = 331

# Oben rechts
x5 = 878
y5 = 331

def paintExe():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('%windir%\system32\mspaint.exe')
    pyautogui.press('enter')

def mouseWalk():
    pyautogui.moveTo(x1, y1)
    for i in range(5):
        if i == 0:
            pyautogui.dragTo(x2, y2, button = 'left')
        elif i == 1:
            pyautogui.dragTo(x3, y3, button = 'left')
        elif i == 2:
            pyautogui.dragTo(x4, y4, button = 'left')
        elif i == 3:
            pyautogui.dragTo(x5, y5, button = 'left')
        elif i == 4:
            pyautogui.dragTo(x1, y1, button = 'left')

paintExe()
mouseWalk()
