#coding=utf-8
#author='Shichao-Dong'

import os,platform
import subprocess
import re
import yaml

import sys
sys.path.append("..")
from file_util import *

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

dev_list =[]
def get_devices():
    devices = []
    result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    # print(result[1].decode())
    # print(len(result))
    if len(result)-2 == 1:
        for line in result[1:]:
            devices.append(line.strip().decode())
        # print(devices[0].split()[0])
        return devices[0].split()[0]
    else:
        print('No device')
        return 'No device found'

    # return devices[0]


#获取mem占用情况
mem_list = []
def mem_common(packagename,f):
    lines = os.popen("adb shell dumpsys meminfo " + packagename).readlines()  # 逐行读取
    total = "TOTAL"
    for line in lines:
        if re.findall(total, line):  # 找到TOTAL 这一行
            lis = line.split(" ")  # 将这一行，按空格分割成一个list
            while '' in lis:  # 将list中的空元素删除
                lis.remove('')
            # return lis[1] #返回总共内存使用
            mem_data = round(int(lis[1]) / 1024, 2)
            print(packagename+'的内存是：'+str(mem_data))
            print(mem_data,file=f,end=',')
            return mem_data

#获取cpu
cpu_list=[]
def cpu_common(packagename,f):
    cmd = 'adb -s ' + get_devices() + ' shell top -n 1| findstr ' + packagename
    top_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    a = (str(top_info[0]))
    # print('前端应用的CPU是：',a)
    pattern = re.compile("\s(\d+)%")
    cpu_data = pattern.search(a).groups()[0]
    print(packagename+'的CPU是：'+str(cpu_data))
    print(cpu_data, file=f, end=',')
    return cpu_data


def get_adb_info(f,yaml_path):
    # 用with的写法是就算没有关闭文件夹，也可以打开文件
    try:
        with open(get_base_path() + yaml_path,'r',encoding='utf-8') as file:
            data=yaml.load(file)
        print(data)
        a=data['process']
        # # mem_common(data['process'])
        # print(a)
        mems = []
        for b in a.values():
            # print(b)
            mem = mem_common(b,f)
            mems.append(mem)
        mem_sum = 0
        for i in range(len(mems)):
            print(str(mems[i]))
            mem_sum = mem_sum +  mems[i]
        print(mem_sum,file=f, end=',')
        # mems.append(mem_sum)

        cpus = []
        for b in a.values():
            cpu = cpu_common(b,f)
            cpus.append(cpu)

        cpu_sum=0
        for i in range(len(cpus)):
            print(str(cpus[i]))
            cpu_sum = cpu_sum +  float(cpus[i])

        print(cpu_sum,file=f)
    except Exception as e:
        print("意外错误：", e)
    # print(mems)


if __name__ == "__main__":
     get_adb_info()
