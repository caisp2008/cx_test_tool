# -*- coding: utf-8 -*-
import threading
import tkinter as tk # imports
from tkinter import ttk
from flow.get_flow import flow


global test_time
test_time=1
def chose_project():
    global text_flow_info
    global test_time

    mg = v.get()

    if mg == 1:
        print('选择了运行10S')
        test_time=10
    if mg == 2:
        print('选择了运行2小时')
        test_time =1800



def init_tab7(tab_page):
    global text_flow_info
    monty = ttk.LabelFrame(tab_page, text=' ')
    monty.grid(column=0, row=0, padx=20, pady=20)

    # tk.Label(monty, text="请选择需要测试的项目:", font=("Arial", 11), width=20, height=2).grid(column=0, row=0, sticky='W',
    #                                                                                  padx=10, pady=10)



    tk.Label(monty, text="测试方法：点击所有一二级页面，退回首页，按home键，记录流量值a；2h之后记录流量值b，两个时间相减，就为这2个小时消耗的流量。", font=("Arial", 11), width=103, height=2).grid(column=0, row=1, sticky='W',
                                                                                     padx=10, pady=10)
    tk.Label(monty, text="测试目的：测试是否存在偷跑流量的情况。", font=("Arial", 11), width=33, height=2).grid(column=0, row=2, sticky='W',
                                                                                     padx=10, pady=10)
    # v = tk.IntVar()
    # v.set(1)
    # tk.Radiobutton(monty, text='酷狗音乐', font=("Arial", 11), width=10, height=2,variable=v,value=1).grid(column=1, row=0, sticky='W', padx=5,pady=5)
    # tk.Radiobutton(monty, text='酷狗铃声', font=("Arial", 11), width=10, height=2,variable=v,value=2).grid(column=2, row=0, sticky='W', padx=10, pady=5)
    # tk.Radiobutton(monty, text='5sing  ', font=("Arial", 11), width=10, height=2,variable=v,value=3).grid(column=3, row=0, sticky='W', padx=5, pady=5)
    # tk.Radiobutton(monty, text='酷狗唱唱', font=("Arial", 11), width=10, height=2,variable=v,value=4).grid(column=4, row=0, sticky='W',padx=10, pady=5)
    # tk.Radiobutton(monty, text='酷狗KTV ', font=("Arial", 11), width=10, height=2,variable=v,value=5).grid(column=5, row=0, sticky='W',padx=10, pady=5)
    tk.Label(monty, text="请选选择测试时长：", font=("Arial", 11), width=15, height=2).grid(column=0, row=3, sticky='W',
                                                                                     padx=10, pady=10)
    global v
    v= tk.IntVar()
    v.set(1)
    tk.Radiobutton(monty, text='10S（用户调试用）', font=("Arial", 11), width=15, height=2,variable=v,value=1,command=chose_project).grid(column=0, row=3, sticky='S', padx=5,pady=5)
    tk.Radiobutton(monty, text='2小时（正常的测试时长）', font=("Arial", 11), width=20, height=2,variable=v,value=2,command=chose_project).grid(column=0, row=3, sticky='E', padx=10, pady=5)

    tk.Button(monty, text='开始测试', font=("Arial", 12), width=15, height=1,command=lambda: run_test(test_time)).grid(column=0, row=7, sticky='W', padx=20,
                                                                               pady=10)
    # tk.Button(monty, text='结束测试', font=("Arial", 12), width=15, height=1).grid(column=0, row=8, sticky='W', padx=20,pady=10)

    text_flow_info = tk.Text(monty, width=70, height=9, font=("Arial", 12))
    text_flow_info.grid(column=0, row=8, sticky='W', padx=20, pady=10)

    tk.Label(monty, text="        ", font=("Arial", 11), width=15, height=2).grid(column=0, row=10, sticky='W',
                                                                                   padx=10, pady=10)



def run_flow(time):
    flow_info1,flow_info2,flow_info3,flow_info4,flow_info5=flow(time)
    # text_flow_info.delete(1.0, tk.END)
    text_flow_info.insert(1.0, flow_info1+flow_info2+flow_info3+flow_info4+flow_info5)


def run_test(time):

    th = threading.Thread(target=run_flow,args=(time,))
    th.setDaemon(True)  # 守护线程
    th.start()

