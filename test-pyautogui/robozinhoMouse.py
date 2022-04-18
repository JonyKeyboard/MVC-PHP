import pyautogui

#automação do teclado
pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')

pyautogui.click('test-pyautogui\circulo.png')

pyautogui.move(0,100)

pyautogui.drag(xOffset=200,yOffset=200,duration=5)