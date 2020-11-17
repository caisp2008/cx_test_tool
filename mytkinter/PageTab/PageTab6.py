# -*- coding: utf-8 -*-
import threading
import time
import tkinter as tk # imports
from tkinter import ttk
import yaml
import re
import datetime
from openpyxl import load_workbook

from monkey_test.adb_common import get_monkey_info, get_data
from monkey_test.write_performance_data import write_kugouring_excel, creat_excel
from monkey_test.monkey import run_monkey, getMonkeyLog
import os
from openpyxl.chart import LineChart, Reference

import sys
sys.path.append("..")
from file_util import *

global projectid,path_report,path_yaml
projectid=1
path_report=get_base_path() + 'Folder\APP_monkey_folder\\report'
path_yaml = get_base_path() + 'Folder\APP_monkey_folder\yaml '

global run_times
run_times=1000

def init_tab6(tab_page):
    global text_monkey_info
    monty = ttk.LabelFrame(tab_page, text=' ')
    monty.grid(column=0, row=0, padx=20, pady=20)
    tk.Button(monty, text='环境配置：点击下载傻猴APP ', font=("Arial", 11), width=45, height=1,command=install_package).grid(column=0, row=2, sticky='W', padx=20, pady=10)
    # tk.Label(monty, text="性能请使用PerfDog进行查看", font=("Arial", 11), width=38, height=2).grid(column=0, row=4,sticky='W',padx=10, pady=10)
    tk.Button(monty, text='环境配置：运行adb tcpip 5555 ', font=("Arial", 11), width=45, height=1,command=run_dalvikvm).grid(column=0, row=3, sticky='W', padx=20, pady=10)

def install_package_tab():
    file_dir = get_base_path() + 'Folder\\bi_folder\package'
    for root, dirs, files in os.walk(file_dir):
        print(files)  # 当前路径下所有非目录子文件
        print(dirs)  # 当前路径下所有子目录
        file_package = file_dir + '\\' + files[0]
        cmd = "adb install " + file_package
        print("运行脚本是：" + cmd)
        os.system(cmd)

def get_dalvikvm():
    cmd = 'adb tcpip 5555'
    print("运行脚本是：" + cmd)
    assist_result = os.system(cmd)
    print(assist_result)
    if assist_result == 0:
        tk.messagebox.showinfo("Message", '链接成功')  # 弹出消息窗口
    else:
        tk.messagebox.showinfo("Message", '连接失败')  # 弹出消息窗口


def run_dalvikvm():
    th = threading.Thread(target=get_dalvikvm())
    th.setDaemon(True)  # 守护线程
    th.start()

def install_package():
    th = threading.Thread(target=install_package_tab)
    th.setDaemon(True)  # 守护线程
    th.start()

