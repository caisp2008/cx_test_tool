# -*- coding: utf-8 -*-
import threading
import tkinter as tk # imports
from tkinter import ttk, END
import time
import re
import csv
import sys
from numpy import *
sys.path.append("..")
from file_util import *

global projectid,path_report,path_yaml
projectid=1
path_report=get_base_path() + 'Folder\APP_monkey_folder\\report'
path_yaml = get_base_path() + 'Folder\APP_monkey_folder\yaml '

global run_times
run_times=1000

def init_tab11(tab_page):
    global text_monkey_info,text_device_info,text_averagedata_info
    monty = ttk.LabelFrame(tab_page, text=' ')
    monty.grid(column=0, row=0, padx=20, pady=20)
    #点击开始采集指标控件
    tk.Button(monty, text='点击开始：酷狗音乐APP性能测试 ', font=("Arial", 11), width=45, height=1,command=run_performance_indicators).grid(column=0, row=0, sticky='W', padx=20, pady=10)
    #点击开始计算平均值
    tk.Button(monty, text='点击开始：计算平均值 ', font=("Arial", 11), width=45, height=1,
              command=run_start_get_averge).grid(column=1, row=0, sticky='W', padx=20, pady=10)
    tk.Button(monty, text='点击结束：计算平均值 ', font=("Arial", 11), width=45, height=1,
              command=end_get_averge).grid(column=1, row=1, sticky='W', padx=20, pady=10)
    #展示实时数据文本框
    text_device_info = tk.Text(monty, width=70, height=25, font=("Arial", 12))
    text_device_info.grid(column=0, row=2, sticky='W', padx=20, pady=10)

    # 展示平均值文本数据
    text_averagedata_info = tk.Text(monty, width=50, height=25, font=("Arial", 12))
    text_averagedata_info.grid(column=1, row=2, sticky='W', padx=20, pady=10)


#采集内存数据方法
def get_memory(package_name, phone_id=''):
        phone_name = ''
        total_mem = ''
        if phone_id:
            phone_name = f" -s {phone_id}"
        cmd = f'adb{phone_name} shell dumpsys meminfo {package_name}'
        contents = os.popen(cmd).read()
        if 'TOTAL:' in contents:
            total_mem = re.findall(r'TOTAL:\s+(\d+)', contents, re.MULTILINE)
        elif 'TOTAL PSS:' in contents:
            total_mem = re.findall(r'TOTAL PSS:\s+(\d+)', contents, re.MULTILINE)
        elif 'com.kugou.android.message' in contents:
            total_mem = re.findall(r'(\d+\,\d+)K: com.kugou.android \(pid', contents, re.MULTILINE)
            total_mem = total_mem[3] if len(total_mem) > 4 else total_mem[0]
            total_mem = ["".join(total_mem.split(','))]
        if total_mem:
            result = eval('int(total_mem[0])/1024')
            return format(result, '.2f')
        else:
            return 0

#获取手机设备方法
def get_devices():
        cmd = f'adb devices'
        contents = os.popen(cmd).read()
        devices_list = re.findall(r'(\w+)\s+device$', contents, re.MULTILINE)
        return devices_list

#多线程
def run_get_devices():
    th = threading.Thread(target=get_performance_indicators(get_devices))
    th.setDaemon(True)  # 守护线程
    th.start()


#获取CPU数据方法
def get_cpu():
        pid_front = ['']
        pid_backend = ['']
        # 获取pid
        cmd_ps = 'adb shell ps -ef'
        cmd_ps_low = 'adb shell ps'
        try:
            contents_pid = os.popen(cmd_ps).read()
            if 'kugou' not in contents_pid:
                contents_pid = os.popen(cmd_ps_low).read()
            pid_front = re.findall(r'\s+(\d+).*com\.kugou\.android(?!\.)', contents_pid, re.MULTILINE)
            pid_backend = re.findall(r'\s+(\d+).*com\.kugou\.android.support', contents_pid, re.MULTILINE)
            # print(pid_front, pid_backend)
            # 根据pid筛选前后台进程
            if pid_front and pid_backend:
                cmd_top = 'adb shell top -n 1'
                contents_cpu = os.popen(cmd_top).read()
                # 前台
                cpu_front = re.findall(f"{pid_front[0]}.*\w\s(\d+\.\d+).*com\.kugou\.and", contents_cpu, re.MULTILINE)
                cpu_front = cpu_front if cpu_front else re.findall(f"{pid_front[0]}.*(\d+%).*com\.kugou\.and",
                                                                   contents_cpu,
                                                                   re.MULTILINE)
                # 后台
                cpu_backend = re.findall(f"{pid_backend[0]}.*\w\s(\d+\.\d+).*com\.kugou\.and", contents_cpu,
                                         re.MULTILINE)
                cpu_backend = cpu_backend if cpu_backend else re.findall(f"{pid_backend[0]}.*(\d+%).*com\.kugou\.and",
                                                                         contents_cpu, re.MULTILINE)
                # print(cpu_front, cpu_backend)
                return [cpu_front[0] if cpu_front else 0, cpu_backend[0] if cpu_backend else 0]
            else:
                return [0, 0]
        except Exception as e:
            return [0, 0]

global is_running
#采集性能方法
def get_performance_indicators(package_name):
    # -*- encoding=utf-8 -*-
    global is_running
    is_running = False
    text_device_info.delete(1.0, END) #清除性能数据
    package_front = "com.kugou.android"  # 前台进程名字
    package_backend = "com.kugou.android.support"  # 后台进程名字
    duration = int(sys.argv[1]) if len(sys.argv) > 2 else 10  # 单位：分钟
    devices = get_devices()  # 获取机型
    csv_header = ["time", "前台Mem", "后台Mem", "前台CPU", "后台CPU"]

    print(f"当前机型deviceID：{devices}")
    set_device_info(f"当前机型deviceID：{devices}\n")
    with open('kugou_cpu_mem.csv', 'a+') as k:
        k_csv = csv.writer(k)
        k_csv.writerow(devices)
        k_csv.writerow(csv_header)
    if len(devices) >= 2:
        print(f"more than one device:{devices}")
    else:
        for item in range(duration * 60):
            if is_running == True:
                break
            record_time = time.strftime('%H:%M:%S', time.localtime())  # 时间
            mem_data_front = get_memory(package_front)  # 前台进程内存
            time.sleep(0.5)
            mem_data_backend = get_memory(package_backend)  # 后台进程内存
            cpu_data = get_cpu()
            data=f"time:{record_time}      前台Mem: {mem_data_front}     后台Mem: {mem_data_backend}     前台CPU: {cpu_data[0]}    后台cpu: {cpu_data[1]} \n"
            # print(f"time:{record_time}      前台Mem: {mem_data_front}     后台Mem: {mem_data_backend}     "
            #       f"前台CPU: {cpu_data[0]}    后台cpu: {cpu_data[1]}")
            # print(data)
            set_device_info(data)
            time.sleep(0.5)
            with open('kugou_cpu_mem.csv', 'a+', newline='') as k:
                k_csv = csv.writer(k)
                k_csv.writerow([record_time, mem_data_front, mem_data_backend, cpu_data[0], cpu_data[1]])

#开始采集性能平均值方法
global Reception_list_mem,backstage_list_mem,Reception_list_CPU,Backstage_list_CPU
def get_data_average(package_name):
    # -*- encoding=utf-8 -*-
    global is_running,Reception_list_mem,backstage_list_mem,Reception_list_CPU,Backstage_list_CPU
    #清楚平均值数据
    text_averagedata_info.delete(1.0, END)
    is_running = True
    package_front = "com.kugou.android"  # 前台进程名字
    package_backend = "com.kugou.android.support"  # 后台进程名字
    duration = int(sys.argv[1]) if len(sys.argv) > 2 else 10  # 单位：分钟
    devices = get_devices()  # 获取机型
    csv_header = ["time", "前台Mem", "后台Mem", "前台CPU", "后台CPU"]

    print(f"当前机型deviceID：{devices}")
    # set_device_info(f"当前机型deviceID：{devices}\n")
    with open('kugou_cpu_mem.csv', 'a+') as k:
        k_csv = csv.writer(k)
        k_csv.writerow(devices)
        k_csv.writerow(csv_header)
    if len(devices) >= 2:
        print(f"more than one device:{devices}")
    else:
        Reception_list_mem = []
        backstage_list_mem = []
        Reception_list_CPU = []
        Backstage_list_CPU = []
        for item in range(duration * 60):
            if is_running == False :
                break
            record_time = time.strftime('%H:%M:%S', time.localtime())  # 时间
            mem_data_front = get_memory(package_front)  # 前台进程内存
            time.sleep(0.5)
            mem_data_backend = get_memory(package_backend)  # 后台进程内存
            cpu_data = get_cpu()
            data=f"time:{record_time}      前台Mem: {mem_data_front}     后台Mem: {mem_data_backend}     前台CPU: {cpu_data[0]}    后台cpu: {cpu_data[1]} "
            set_device_info(data+"\n")
            # print("mem_data_front是这个："+mem_data_front)
            #把内存存到内存列表中
            Reception_list_mem.append(mem_data_front)
            backstage_list_mem.append(mem_data_backend)
            Reception_list_CPU.append(cpu_data[0])
            Backstage_list_CPU.append(cpu_data[1])
            print("前台内存列表" + str(Reception_list_mem))
            print("后台内存列表" + str(backstage_list_mem))
            print("前台CPU列表" + str(Reception_list_CPU))
            print("后台CPU列表" + str(Backstage_list_CPU))
            time.sleep(0.5)
            with open('kugou_cpu_mem.csv', 'a+', newline='') as k:
                k_csv = csv.writer(k)
                k_csv.writerow([record_time, mem_data_front, mem_data_backend, cpu_data[0], cpu_data[1]])

#打印性能指标多线程
def run_performance_indicators():
    package_name = 'com.kugou.android'
    th = threading.Thread(target=get_performance_indicators,args=(package_name,))
    th.setDaemon(True)  # 守护线程
    th.start()

#开始计算平均值多线程
def run_start_get_averge():
    # 开始采集需要计算平均值的数据
    # print("开始计算以下数据平均值")
    set_device_info("\n——————————————开始计算数据平均值————————————————\n")
    set_averagedata_info('开始计算数据平均值\n')
    package_name = 'com.kugou.android'
    th = threading.Thread(target=get_data_average, args=(package_name,))
    th.setDaemon(True)  # 守护线程
    th.start()

#结束计算平均值多线程
def end_get_averge():
    # 开始采集需要计算平均值的数据
    #定义is_running全局变量
    global is_running,Reception_list_mem,backstage_list_mem,Reception_list_CPU,Backstage_list_CPU
    set_averagedata_info('结束计算数据平均值\n')
    is_running = False
    #计算前台内存的平均值
    b = len(Reception_list_mem)
    sum = 0
    for i in Reception_list_mem:
        sum = sum + float(i)
    print(sum / b)
    #打印前台内存list
    set_averagedata_info(str(Reception_list_mem)+"\n")
    set_averagedata_info("前台内存平均值是：" + str(float(sum / b)) + "\n\n" )

    # 计算后台内存的平均值
    b = len(backstage_list_mem)
    sum = 0
    for i in backstage_list_mem:
        sum = sum + float(i)
    print(sum / b)
    # 打印后台内存list
    set_averagedata_info(str(backstage_list_mem)+"\n")
    set_averagedata_info("后台内存平均值是：" + str(float(sum / b)) + "\n\n")

    # 计算前台CPU的平均值
    b = len(Reception_list_CPU)
    sum = 0
    for i in Reception_list_CPU:
        sum = sum + float(i)
    print(sum / b)
    # 打印前台CPU list
    set_averagedata_info(str(Reception_list_CPU)+"\n")
    set_averagedata_info("前台CPU平均值是：" + str(float(sum / b)) + "\n\n")

    # 计算后台CPU的平均值
    b = len(Backstage_list_CPU)
    sum = 0
    for i in Backstage_list_CPU:
        sum = sum + float(i)
    print(sum / b)
    # 打印前台CPU list
    set_averagedata_info(str(Backstage_list_CPU) + "\n")
    set_averagedata_info("后台CPU平均值是：" + str(float(sum / b)) + "\n\n")

#把性能数据打印出来
def set_device_info(data):
    # text_device_info.delete(1.0, END)
    text_device_info.insert(tk.END,data)

#把平均值数据打印出来
def set_averagedata_info(data):
    # text_device_info.delete(1.0, END)
    text_averagedata_info.insert(tk.END,data)