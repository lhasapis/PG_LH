
import pyautogui as pg
import time

pg.hotkey('winleft','ctrl','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.3)
pg.hotkey('winleft','up')
pg.typewrite('https://www.youtube.com/watch?v=ZY3J3Y_OU0w\n',0.3)
time.sleep(20)
pg.hotkey('ctrl','t')
pg.typewrite('http://www.foodnetwork.com/recipes/food-network-kitchen/classic-hot-chocolate-3364191\n',0.3)



