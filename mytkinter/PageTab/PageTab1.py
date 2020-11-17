# -*- coding: utf-8 -*-
import re
import tkinter as tk # imports
from tkinter import ttk, END
import os
import subprocess
import datetime
import threading
import time
# from performance_monkey_test.adb import adb_kugou
from file_util import get_base_path
path_package = get_base_path() + 'Folder\APP_xn_auto_folder\package'

def init_tab1(tab_page):
    global text_device_info,text_device_packagename,text_device_activityname,switchscrBtn,text_kugouinfo,text_filename,installButton

    monty = ttk.LabelFrame(tab_page, text=' ')
    monty.grid(column=0, row=0, padx=20, pady=20)
    tk.Button(monty, text='检测手机是否连接成功', font=("Arial", 11), width=30, height=1,command=deviceinfo).grid(column=0, row=1, sticky='W',padx=20, pady=10)
    text_device_info = tk.Text(monty, width=50, height=1, font=("Arial", 12))
    text_device_info.grid(column=1, row=1, sticky='W', padx=20, pady=10)

    tk.Button(monty, text='查看当前页面的包名', font=("Arial", 11), width=30, height=1,command=getpackagename).grid(column=0, row=3, sticky='W',padx=20, pady=10)
    text_device_packagename=tk.Text(monty, width=50, height=1, font=("Arial", 12))
    text_device_packagename.grid(column=1, row=3, sticky='W', padx=20, pady=10)


    tk.Button(monty, text='请将测试包放在该文件夹\n并删除之前的包', font=("Arial", 12), width=30, height=2,
              command=lambda: open_world(path_package)).grid(column=0, row=4, sticky='W', padx=20,
                                                             pady=10)

    tk.Button(monty, text='点击安装测试包', font=("Arial", 12), width=30, height=2, command=install_package).grid(column=1,
                                                                                                           row=4,
                                                                                                           sticky='W',
                                                                                                           padx=20,
                                                                                                           pady=10)

    tk.Button(monty, text='点击查看性能测试报告_总模板', font=("Arial", 11), width=30, height=2, command=open_report).grid(column=1, row=7,
                                                                                                    sticky='W', padx=20,
                                                                                                    pady=10)

    tk.Button(monty, text='APP截屏', font=("Arial", 11), width=30, height=2, command=screenshot).grid(column=0,row=21,sticky='W',padx=20,pady=10)
    switchscrBtn=tk.Button(monty, text='开始录像', font=("Arial", 11), width=30, height=2,command=switchscreenrecord)
    switchscrBtn.grid(column=1, row=21, sticky='W', padx=30,pady=10)
    tk.Button(monty, text='查看截屏和录像', font=("Arial", 11), width=20, height=2,command=openVideoPhoto).grid(column=2, row=21, sticky='W', padx=20,pady=50)


#获取设备信息
def set_device_info(devices_name):
    text_device_info.delete(1.0, END)
    text_device_info.insert(1.0, devices_name)

def deviceinfo():
    ##获取设备多台设备号列表
        str_init = ' '
        all_info = os.popen('adb devices').readlines()
        print('adb devices 输出的内容是：', all_info)

        for i in range(len(all_info)):
            str_init += all_info[i]
        devices_name = re.findall('\n(.+?)\t', str_init, re.S)

        if len(devices_name) > 0:
            print('所有设备名称：\n', devices_name)
            set_device_info(devices_name)
            return devices_name
        else:
            tk.messagebox.showerror(title='出错了！', message='设备连接失败')


#获取包名
def set_device_packagename(devpackage):
    text_device_packagename.delete(1.0,END)
    text_device_packagename.insert(1.0,devpackage)

def getpackagename():
    pattern = re.compile(r"[a-zA-Z0-9\.]+/.[a-zA-Z0-9\.]+")
    package = subprocess.Popen("adb shell dumpsys window | findstr mCurrentFocus", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
    # print(package)
    package =  (str(package))
    # print(package)
    packagename = pattern.findall(package)[0].split('/')[0]

    if len(packagename) > 0:
        print(packagename)
        set_device_packagename(packagename)
    else:
        tk.messagebox.showerror(title='出错了！', message='获取包名失败')



#获取activity
def set_device_activityname(devactivity):
    text_device_activityname.delete(1.0,END)
    text_device_activityname.insert(1.0,devactivity)

def getactivity():
    pattern = re.compile(r"[a-zA-Z0-9\.]+/.[a-zA-Z0-9\.]+")
    package = subprocess.Popen("adb shell dumpsys window | findstr  mFocusedActivity", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
    package =  (str(package))
    activityname = pattern.findall(package)[0].split('/')[1]
    set_device_activityname(activityname)

    # print(activity)
    # return activity

# 截图函数
def screenshot():
        nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        name = nowtime + '.png'
        out = subprocess.getstatusoutput('adb shell screencap -p /sdcard/screen.png')


        path = get_base_path() + 'mytkinter\VideoPhoto\{}'


        # out1 = subprocess.getstatusoutput('adb pull /sdcard/screen.png ./VideoPhoto/{}'.format(name))
        out1 = subprocess.getstatusoutput('adb pull /sdcard/screen.png ' + path.format(name))

        print(out1)
        if out[0] == 0 and out1[0] == 0:
            pass
        else:
            tk.messagebox.showinfo("Message", "未知原因，截图失败")  # 弹出消息窗口


#录像
def switchscreenrecord():
    if  switchscrBtn['text'] == '开始录像':
        switchscrBtn['text'] = '结束录像'
        startrecord()

    else:
        switchscrBtn['text'] = '开始录像'
        endrecord()


def startrecord():
        global name1,out,pro
        nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        name1 = nowtime + 'test.mp4'
        out = 'adb shell screenrecord /sdcard/test.mp4'
        print('录像开始')
        pro = subprocess.Popen(out, stderr=subprocess.PIPE)

# 结束进程
def endrecord():
        path = get_base_path() + 'mytkinter\VideoPhoto\{}'
        pro.kill()
        print('录像结束')
        subprocess.getstatusoutput('adb pull /sdcard/test.mp4 '+ path.format(name1))  # .close()是关闭文件的   .kill（）是杀掉进程

def openVideoPhoto():

    path = get_base_path() + 'mytkinter\VideoPhoto'
    os.startfile(path)

    # rootdir = 'D:\python_workspaces\cx_test_tool\mytkinter\VideoPhoto'
    # os.open(rootdir)  # 列出文件夹下所有的目录与文件

def run_test():
    th = threading.Thread(target=set_text_test)
    th.setDaemon(True)  # 守护线程
    th.start()

def set_text_test():
    global get_adb_kugou_isrun
    get_adb_kugou_isrun = True
    i=1

def get_adb_kugou_stop():
    global get_adb_kugou_isrun
    get_adb_kugou_isrun = False

def set_filename(filename):
    text_filename.delete(1.0,END)
    text_filename.insert(1.0,filename)



def endinstall():
        pro.kill()

def open_report():
    # path = '..\性能测试报告模板'
    path = get_base_path() + '\性能测试报告模板'
    path = os.path.abspath(path)  # 获取当前脚本所在的路径
    os.startfile(path)

def install_package_tab():
    file_dir = get_base_path() + 'Folder\APP_xn_auto_folder\package'
    for root, dirs, files in os.walk(file_dir):
        print(files)  # 当前路径下所有非目录子文件
        print(dirs)  # 当前路径下所有子目录
        file_package = file_dir + '\\' + files[0]
        cmd = "adb install " + file_package
        print("运行脚本是：" + cmd)
        os.system(cmd)

#多线程安装包
def install_package():
    th = threading.Thread(target=install_package_tab)
    th.setDaemon(True)  # 守护线程
    th.start()

def open_world(path):

    path = os.path.abspath(path)  # 获取当前脚本所在的路径
    os.startfile(path)

if __name__ == "__main__":
   deviceinfo()
   # getpackagename()
   # openVideoPhoto()
   # get_kugouinfo()
   # print(os.path.abspath('..\VideoPhoto'))
   # os.startfile(os.path.abspath('..\VideoPhoto'))