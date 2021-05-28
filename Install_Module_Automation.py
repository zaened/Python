import pyautogui

pyautogui.hotkey('win', 'r')
pyautogui.typewrite('cmd')
pyautogui.press('enter')
pyautogui.typewrite('cd AppData\\Local\\Programs\\Python\\Python38')
pyautogui.press('enter')
pyautogui.typewrite('pip install')
