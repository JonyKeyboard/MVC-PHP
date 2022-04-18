import pyautogui

#automação do teclado
pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')

pyautogui.write('Esta funcionando! ')