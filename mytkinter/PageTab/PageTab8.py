# -*- coding: utf-8 -*-
import tkinter as tk # imports
from tkinter import ttk
import os

import sys
sys.path.append("..")
from file_util import *

def init_tab8(tab_page):
    global text_device_info
    monty = ttk.LabelFrame(tab_page, text=' ')
    monty.grid(column=0, row=0, padx=20, pady=20)

    tk.Button(monty, text='点击打开过度绘制工具 ', font=("Arial", 11), width=20, height=1 , command = openPath ).grid(column=0, row=1, sticky='W', padx=20,
                                                                 pady=10)

    tk.Label(monty, text="使用说明：\n                                                                          1、打开文件夹后，运行“过度绘制.exe”文件\n                                                                               2、过度绘制占比一般大于等于50%都是有问题\n                                                                                  "
                         "3、overdraw文件夹可以查看过度绘制问题的图片\n"
                         "手机配置：\n                                                              1、测试过程一定要进入开发者模式\n                                                 2、把过度绘制的开关打开\n                                                                           3、不要把过度绘制的标准为0或者超过100",font=("Arial", 11), width=80, height=10).grid(column=0,
                                                                                                               row=6,
                                                                                                               sticky='W',
                                                                                                               columnspan=6,
                                                                                                               padx=10,
                                                                                                               pady=10)

def openPath():
    path = get_base_path() + 'Tools\GPU_tools'
    path = os.path.abspath(path)  # 获取当前脚本所在的路径
    os.startfile(path)
