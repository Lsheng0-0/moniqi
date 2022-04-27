# -*- coding: UTF-8 -*-
from time import sleep

# 大漠初始化注册


dm.createDm()
dm = dm.reg()
ret = dm.reg("639833479a324fd414703817ac72d1b5dca9fd", "7788990")
print(ret)
if ret == 1:
    print("注册成功")
else:
    print("注册失败")

hwnd = dm.EnumWindow(0, "canvas", "canvasWin", 1 + 2)
hwnd = int(hwnd)
print(hwnd)
dm_Set = dm.SetWindowState(hwnd, 1)
dm_Force = dm.ForceUnBindWindow(hwnd)

dm_bind = dm.BindWindow(hwnd, "normal", "normal", "normal", 0)
sleep(1)
if dm_bind == 1:
    print("绑定成功")
else:
    print("绑定失败")
