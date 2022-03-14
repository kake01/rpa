import pyautogui as pg
import time
# import myvector


tabClickNum = 5

# Miroを開く
pg.press('win')
pyperclip.copy('Miro')
pg.hotkey('ctrl','v')
pg.press('enter')
#　起動まで15秒待つ
time.sleep(15)

# 最大化してダッシュボードを開く
pg.hotkey('ctrl', 'win', "up")
pg.moveTo(30, 80, 1)
pg.click()
pg.moveTo(150, 200, 1)
pg.click()
# 下の値は変数
pg.moveTo(413, 542, 1)
pg.click()
time.sleep(15)
print('ダッシュボード展開don')


pg.moveTo(35, 630, 1)
pg.click()
pg.moveTo(110, 550, 1)
pg.click()


for i in range(tabClickNum):
    pg.moveTo(35, 630, 1)
    pg.click()
    pg.moveTo(110, 550, 1)
    pg.click()
print('ダッシュボード展開don')
