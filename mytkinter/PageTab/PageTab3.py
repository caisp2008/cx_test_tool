# -*- coding: utf-8 -*-
import tkinter as tk # imports
from tkinter import ttk
from tkinter import *
from mytkinter.PageTab.TestCase import *

n=3
def init_tab3(tab_page):
    global text_device_info
    global row_index
    casies = []

    row_index =2
    v = StringVar()
    monty = ttk.LabelFrame(tab_page, text=' ')
    monty.grid(column=0, row=0, padx=20, pady=20)

    # tk.Label(monty, text="测试地址: ", font=("Arial", 11), width=20, height=2).grid(column=0, row=0, sticky='W',
    #                                                                                  padx=10, pady=10)
    # text_url_info=tk.Text(monty, width=37, height=1, font=("Arial", 12))
    # text_url_info.grid(column=1, row=0, sticky='W', padx=20, pady=10)
    # text_url_info.insert(1.0,'   http://172.17.8.134:8989/api/debugtalk_list/1/')
    #
    # tk.Label(monty, text="测试教程:", font=("Arial", 11), width=20, height=2).grid(column=0, row=1, sticky='W',
    #                                                                                  padx=10, pady=10)
    # text_jiaocheng_info = tk.Text(monty, width=37, height=1, font=("Arial", 12))
    # text_jiaocheng_info.grid(column=1, row=1, sticky='W', padx=20, pady=10)
    # text_jiaocheng_info.insert(1.0, '   https://sutune.me/2018/08/05/httprunner/')

    tk.Label(monty, text="接口测试用例生成器：", font=("Arial", 11), width=18, height=2).grid(column=0, row=2, sticky='W',padx=5, pady=5)

    #添加新的参数
    def add_tab(n):
        global row_index
        row_index = n

        tk.Label(monty, text="参数名", font=("Arial", 11), width=10, height=2).grid(column=1, row=n, sticky='W',padx=5, pady=2)
        #写入接口的参数名和类型
        # entry = tk.Entry(monty, textvariable=v, validate='focusout')

        entry= tk.Entry(monty)
        entry.grid(column=2, row=n, sticky='W',padx=5, pady=2)

        test_case = TestCase()
        test_case.set_param_name(entry)
        casies.append(test_case)

        tk.Label(monty, text="参数类型", font=("Arial", 11), width=10, height=2).grid(column=3, row=n, sticky='W',padx=5, pady=2)

        cmb = ttk.Combobox(monty, width=5, height=2)
        cmb.grid(column=4, row=n, sticky='W', padx=5, pady=2)
        # 设置下拉菜单中的值
        cmb['value'] = ('string', 'int', 'float')
        # 设置默认值，即默认下拉框中的内容
        cmb.current(0)
        # 默认值中的内容为索引，从0开始

        tk.Label(monty, text="是否必填", font=("Arial", 11), width=8, height=2).grid(column=5, row=n, sticky='W', padx=5,
                                                                                  pady=2)
        cmb1 = ttk.Combobox(monty, width=5, height=2)
        cmb1.grid(column=6, row=n, sticky='W', padx=5, pady=2)
        # 设置下拉菜单中的值
        cmb1['value'] = ('是', '否')
        # 设置默认值，即默认下拉框中的内容
        cmb1.current(1)
        # 默认值中的内容为索引，从0开始


    add_tab(2)
    #添加参数控件
    tk.Button(monty, text=' 添加 ', font=("Arial", 12), width=5, height=1,command=lambda: add_tab(row_index+1)).grid(column=7, row=n,sticky='W', padx=10, pady=2)

    #获取参数输入的内容
    def show():
        for c in casies:
            print(c.get_param_name().get())
    #点击生成用例
    tk.Button(monty, text='点击生成用例',font=("Arial", 12), width=15, height=1,command=show).grid(column=2, row=10, sticky='W', padx=10,pady=10)

    text_monkey_info = tk.Text(monty, width=125, height=10, font=("Arial", 12))
    text_monkey_info.grid(row=15, column=0, sticky='W', columnspan=9, padx=10, pady=10)






