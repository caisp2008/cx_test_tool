
import datetime
import subprocess
import time
import os
import re
import threading
from multiprocessing.dummy import Pool as ThreadPool
import sys
sys.path.append("..")
from file_util import *

import yaml

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

dev_list =[]

dev_list =[]

def get_devices():
    devices = []
    result = os.popen("adb devices ").stdout.readlines()
    # print(result[1].decode())
    #print(len(result))
    if len(result)-2 == 1:
        for line in result[1:]:
            devices.append(line.strip().decode())
        #print(devices[0].split()[0])
        return devices[0].split()[0]
    else:
        print("No device")
        return "No device found"


def Devices():
    Data=[]
    StatusString = ["unauthorized", "device", "offline"]
    for Row in os.popen('adb devices'):
        RowData=Row.strip().split()
        if len(RowData) == 2 :
            if RowData[1] in StatusString:
                Data.append(RowData)
    return Data


def run_monkey(run_times,method):
    # method('monkey测试开始啦\n')
    path_monkey_log = get_base_path() + 'Folder\APP_monkey_folder\log\monkeyLog.txt'
    path_test_log =get_base_path() + 'Folder\APP_monkey_folder\log\determine_log.txt'
    f_test = open(path_test_log, 'w')
    f_monkey = open(path_monkey_log, 'w')
    f_monkey.close()

    with open(get_base_path() + 'performance_function_test/yaml/performance_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    package = data['packageName']
    # print(package)
    # times_monkey = data['frequency']
    # print(times_monkey)
    os.popen(
        "adb shell monkey -p " + package + " --throttle 500 -s 1000 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v " + str(run_times) + " >" + path_monkey_log).read()

    print('monkey测试结束啦，请查看测试结果。。。。。', file=f_test)
    f_test.close()
    getMonkeyLog(method)

def getMonkeyLog(method):
    # 读取monkey日志
    path_monkey_log=get_base_path() + 'Folder\APP_monkey_folder\log\monkeyLog.txt'
    with open( path_monkey_log, "r") as file1:
        content = file1.readlines()

    # 将4种日志信息保存到report文件中
    path_report_log = get_base_path() + 'Folder\APP_monkey_folder\log\\reportLog.txt'

    print('检查monkey日志中。。。\n')
    with open(path_report_log, "a") as file2:
        file2.write(str(datetime.datetime.now()) + '\n')
        str1 = '.*ANR.*'
        str2 = '.*CRASH.*'
        str3 = '.*Exception.*'
        str4 = '.*finished.*'
        Acount, Ccount, Ecount = 0, 0, 0
        for i in content:
            if re.match(str1, i):
                method('测试过程中出现ANR错误\n')
                file2.write(i)
                Acount += 1
            if re.match(str2, i):
                method('测试过程中出现CRASH错误\n')
                file2.write(i)
                Ccount += 1
            if re.match(str3, i):
                method('测试过程中出现Exception错误\n')
                file2.write(i)
                Ecount += 1
        if Acount==0 and Ccount==0 and Ecount == 0:
            for i in content:
                if re.match(str4, i):
                    method('monkey测试过程中正常，无异常崩溃\n')
                    file2.write(i)

if __name__ =="__main__":

    run_monkey()
    getMonkeyLog()


