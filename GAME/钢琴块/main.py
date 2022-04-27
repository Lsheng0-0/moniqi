# -*- coding: UTF-8 -*-
import os
import random
import sys
from time import sleep

import pyautogui

from public import dm

pyautogui.FAILSAFE = True  # 安全模式打开 鼠标移动到左上角终止程序
sleep(3)

for int_x in (67, 216, 363, 508):
    ret_col = dm.GetColorBGR(int_x, 716)
    print(int_x)
    if ret_col == 'c69e31':
        dm.MoveTo(int_x, 716)
        dm.leftclick()
        sleep(1)
        print('(%d,%d)' % (int_x, 716))
        break

while True:
    for int_x in (67, 216, 363, 508):
        ret_col = dm.GetColorBGR(int_x, 716)
        print(ret_col, int_x)
        if ret_col == '000000':
            dm.MoveTo(int_x, 716)
            dm.leftclick()
            sleep(1)
            print('(%d,%d)' % (int_x, 716))
