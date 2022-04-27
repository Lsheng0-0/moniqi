# -*- coding: UTF-8 -*-
from time import sleep

from public import dm


def find_color(int_1x, int_y1, int_x2, int_y2, color, sim, dir):
    #dir 整形数:查找方向 0: 从左到右,从上到下
             # 1: 从左到右,从下到上
             # 2: 从右到左,从上到下
             # 3: 从右到左,从下到上
             # 4：从中心往外查找
             # 5: 从上到下,从左到右
             # 6: 从上到下,从右到左
             # 7: 从下到上,从左到右
             # 8: 从下到上,从右到左

    dm_ret = dm.FindColor(int_1x, int_y1, int_x2, int_y2, color, sim, dir)
    return dm_ret


def find_color_click(int_1x, int_y1, int_x2, int_y2, color, sim, dir):
    dm_ret = find_color(int_1x, int_y1, int_x2, int_y2, color, sim, dir)
    a = dm_ret[0]
    b = dm_ret[1]
    print("(%d,%d)" % (a, b))
    dm.MoveTo(dm_ret[0], dm_ret[1])
    dm.LeftClick()


def find_pic(int_1x, int_y1, int_x2, int_y2, pic_name, delta_color,sim, dir):
    #dir 整形数:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上
    dm_ret = dm.FindPic(int_1x, int_y1, int_x2, int_y2, pic_name, delta_color,sim, dir)
    return dm_ret


def find_pic_click(int_1x, int_y1, int_x2, int_y2, pic_name, delta_color,sim, dir):
    dm_ret = dm.FindPic(int_1x, int_y1, int_x2, int_y2, pic_name, delta_color,sim, dir)
    a = dm_ret[0]
    b = dm_ret[1]
    print("(%d,%d)" % (a, b))
    dm.MoveTo(dm_ret[0], dm_ret[1])
    dm.LeftClick()

def find_str(int_1x, int_y1, int_x2, int_y2,str_name,color_format,sim):
    dm_ret = dm.FindStr(int_1x, int_y1, int_x2, int_y2,str_name,color_format,sim)
    return dm_ret

def find_str_click(int_1x, int_y1, int_x2, int_y2,str_name,color_format,sim):
    dm_ret = dm.FindStr(int_1x, int_y1, int_x2, int_y2,str_name,color_format,sim)
    a = dm_ret[0]
    b = dm_ret[1]
    print("(%d,%d)" % (a, b))
    dm.MoveTo(dm_ret[0], dm_ret[1])
    dm.LeftClick()

