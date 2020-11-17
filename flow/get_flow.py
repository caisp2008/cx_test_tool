#coding=utf-8
#author='Shichao-Dong'

import os,platform
import subprocess
import re
import time


si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

dev_list =[]
def get_devices():
    devices = []
    result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    if len(result)-2 == 1:
        for line in result[1:]:
            devices.append(line.strip().decode())
        return devices[0].split()[0]
    else:
        print('No device')
        return 'No device found'

    # return devices[0]
def getpackagename():
    pattern = re.compile(r"[a-zA-Z0-9\.]+/.[a-zA-Z0-9\.]+")
    package = subprocess.Popen("adb shell dumpsys activity | findstr  mFocusedActivity", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
    package =  (str(package))
    packagename = pattern.findall(package)[0].split('/')[0]
    # print (pattern.findall(package)[0].split('/')[0])
    # print (pattern.findall(package)[0].split('/')[1])
    # print(packagename)
    return packagename

#获取pid和uid
pid_list = []
def pid():
    cmd = 'adb -s '+ get_devices() +' shell ps |findstr com.kugou.android.ringtone'
    pid_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    if len(pid_info)>=1:
        pid_list.append(int(pid_info[0].split()[1]))
        # print('pid是。。。。。。。。。。。。。。'+str(pid_list))
    return str(pid_list[0])

uid_list = []
def uid():
    cmd ='adb -s '+ get_devices() +' shell cat  /proc/'+ pid() + '/status'
    uid_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    if len(uid_info)>= 1:
        uid_list.append(int(uid_info[7].split()[1]))
    return str(uid_list[0])

#获取流量
def rcv_flow():
    cmd = 'adb -s '+ get_devices() +' shell cat /proc/uid_stat/'+uid()+'/tcp_rcv'

    flow_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    print('接收字节数 '+re.findall('\d+', str(flow_info))[0])
    return re.findall('\d+', str(flow_info))[0]

def snd_flow():
    cmd = 'adb -s ' + get_devices() + ' shell cat /proc/uid_stat/' + uid() + '/tcp_snd'
    print(cmd)
    flow_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    print('发送字节数 '+re.findall('\d+', str(flow_info))[0], end='    ')
    return re.findall('\d+', str(flow_info))[0]

def flow(test_time):
    a='测试前数据：   发动字节数  '+snd_flow()
    b='  接收字节数  '+rcv_flow()+'\n'
    time.sleep(int(test_time))
    c='测试后数据：   发动字节数  '+snd_flow()
    d='  接收字节数  '+rcv_flow()+'\n'

    return a,b,c,d,'测试完成了！！！！！！！！！！！！！！！！！'


if __name__ == "__main__":
   time_begin = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
   print('流量测试开始了，请开启要测试的APP。。。。\n   测试方法：点击进入所有一二级页面，退回首页，按home键，记录流量值a；2h之后记录流量值b，两个时间相减，就为这2个小时消耗的流量\n       目的：测试是否存在偷跑流量的情况')
   print('开始时间   '+str(time_begin))

   time_sleep=input('请输入测试时间：')

   before_snd_flow=snd_flow()
   before_rcv_flow = rcv_flow()
   time.sleep(int(time_sleep))
   time_after = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
   print('结束时间   ' + str(time_after))
   after_snd_flow = snd_flow()
   after_rcv_flow = rcv_flow()


