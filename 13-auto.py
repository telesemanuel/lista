import pyautogui as auto
import time

auto.PAUSE = 1.0

auto.press('win')
auto.write('edge')
auto.press('enter')     
auto.hotkey('alt','space')
auto.press('x')
auto.write('youtube.com.br')
auto.press('enter')

time.sleep(3)

for i in range(4):
    auto.press('tab')

auto.write('Python')
auto.press('enter')