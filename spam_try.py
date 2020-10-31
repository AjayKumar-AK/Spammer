import pyautogui ,time
time.sleep(5)
f = open('sapmmer_material','r')
for i in f:
    pyautogui.typewrite(i)
    pyautogui.press('enter')