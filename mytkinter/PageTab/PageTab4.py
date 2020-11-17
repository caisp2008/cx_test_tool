# -*- coding: utf-8 -*-
import os
import subprocess
import threading
import tkinter as tk # imports
from tkinter import ttk

import yaml

from file_util import get_base_path

# 打开yaml文件，并获取包名，进程名等信息
with open(get_base_path() + 'Folder\\bi_folder\\bi.yaml', 'r', encoding='utf-8') as file:
    data = yaml.load(file)
online_bi_umeng_info = data['online_bi_umeng']
new_bi_umeng_info = data['new_bi_umeng']

print(new_bi_umeng_info)

def init_tab4(tab_page):
    global text_monkey_info
    monty = ttk.LabelFrame(tab_page, text=' ')
    monty.grid(column=0, row=0, padx=20, pady=20)

    tk.Button(monty, text="点击配置统计文件", font=("Arial", 11), width=25, height=1,command=open_result).grid(column=0,row=1,sticky='W', padx=20, pady=10)
    tk.Button(monty, text="点击开始测试", font=("Arial", 11), width=25, height=1,command=  lambda: strat_test_bi(new_bi_umeng_info) ).grid(column=0,row=2,sticky='W', padx=20, pady=10)
    tk.Button(monty, text="点击开始测试上线前核心统计", font=("Arial", 11), width=25, height=1, command=lambda: strat_test_bi(online_bi_umeng_info)).grid(column=0,row=3,sticky='W',padx=20,pady=10)
    # tk.Button(monty, text="点击结束测试", font=("Arial", 11), width=25, height=1, command=strat_test_bi).grid(column=0,row=4,sticky='W',padx=20,pady=10)

    text_monkey_info = tk.Text(monty, width=125, height=18, font=("Arial", 12))
    text_monkey_info.grid(row=8, column=0, sticky='W', columnspan=7, padx=10, pady=10)

def open_result():
    path = get_base_path() + 'Folder\\bi_folder'
    path = os.path.abspath(path)  # 获取当前脚本所在的路径
    os.startfile(path)


#需求：检测列表中的值，只要检测到其中任何一个值，就打印出这行日志
#bi测试方法
def test_bi(bi_umeng_info):
    # matchConditions = ["a=16063", "a=14220", "a=14192", "a=8310", "a=8309", "a=16062", "a=16072", "16061", "a=16059",
    #                    "a=16064", "a=15471", "a=15126","umeng"]

    # matchConditions = ["a=20012"]

    # a = "a=16063"
    # 清除日志
    print('开始测试bi')
    c_order = "adb logcat -c"
    c_p = subprocess.Popen(c_order, stdout=subprocess.PIPE, bufsize=1).stdout

    # debug日志打印
    order = "adb logcat"
    p = subprocess.Popen(order, stdout=subprocess.PIPE, bufsize=1).stdout
    for line in iter(p.readline, b''):
        # print(str(line))

        for i in range(len(bi_umeng_info)):
            if bi_umeng_info[i] in str(line):
                print(str(line.decode()))
                insert_text(str(line.decode())+'\n')

#多线程开始测试bi
def strat_test_bi(bi_umeng_info):
    th = threading.Thread(target=test_bi, args=(bi_umeng_info,))
    th.setDaemon(True)  # 守护线程
    th.start()


def insert_text(message):
    text_monkey_info.insert(tk.END, message)



