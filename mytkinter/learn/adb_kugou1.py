import os
import re
import subprocess
import time


def totalCpuTime(devices):
    user=nice=system=idle=iowait=irq=softirq= 0
    '''
    user:从系统启动开始累计到当前时刻，处于用户态的运行时间，不包含 nice值为负进程。
    nice:从系统启动开始累计到当前时刻，nice值为负的进程所占用的CPU时间
    system 从系统启动开始累计到当前时刻，处于核心态的运行时间
    idle 从系统启动开始累计到当前时刻，除IO等待时间以外的其它等待时间
    iowait 从系统启动开始累计到当前时刻，IO等待时间(since 2.5.41)
    irq 从系统启动开始累计到当前时刻，硬中断时间(since 2.6.0-test4)
    softirq 从系统启动开始累计到当前时刻，软中断时间(since 2.6.0-test4)
    stealstolen  这是时间花在其他的操作系统在虚拟环境中运行时（since 2.6.11）
    guest 这是运行时间guest 用户Linux内核的操作系统的控制下的一个虚拟CPU（since 2.6.24）
    '''
    cmd = "adb -s " + devices +" shell cat /proc/stat"
    print(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    res = output.split()

    for info in res:
        if info.decode() == "cpu":
            user = res[1].decode()
            nice = res[2].decode()
            system = res[3].decode()
            idle = res[4].decode()
            iowait = res[5].decode()
            irq = res[6].decode()
            softirq = res[7].decode()
            print("user=" + user)
            print("nice=" + nice)
            print("system=" + system)
            print("idle=" + idle)
            print("iowait=" + iowait)
            print("irq=" + irq)
            print("softirq=" + softirq)
            result = int(user) + int(nice) + int(system) + int(idle) + int(iowait) + int(irq) + int(softirq)
            print("totalCpuTime"+str(result))
            return result



'''
每一个进程快照
'''
def processCpuTime(pid, devices):
    '''

    pid     进程号
    utime   该任务在用户态运行的时间，单位为jiffies
    stime   该任务在核心态运行的时间，单位为jiffies
    cutime  所有已死线程在用户态运行的时间，单位为jiffies
    cstime  所有已死在核心态运行的时间，单位为jiffies
    '''
    utime=stime=cutime=cstime = 0
    cmd = "adb -s "+ devices + " shell cat /proc/" + pid +"/stat"
    print(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    res = output.split()
    utime = res[13].decode()
    stime = res[14].decode()
    cutime = res[15].decode()
    cstime = res[16].decode()
    print("utime="+utime)
    print("stime="+stime)
    print("cutime="+cutime)
    print("cstime="+cstime)
    result = int(utime) + int(stime) + int(cutime) + int(cstime)
    print("processCpuTime="+str(result))
    return result

'''
计算某进程的cpu使用率
100*( processCpuTime2 – processCpuTime1) / (totalCpuTime2 – totalCpuTime1) (按100%计算，如果是多核情况下还需乘以cpu的个数);
cpukel cpu几核
pid 进程id
'''
def cpu_rate(pid, cpukel, devices):
    # pid = get_pid(pkg_name)
    processCpuTime1 = processCpuTime(pid, devices)
    time.sleep(1)
    processCpuTime2 = processCpuTime(pid, devices)
    processCpuTime3 = processCpuTime2 - processCpuTime1

    totalCpuTime1 = totalCpuTime(devices)
    time.sleep(1)
    totalCpuTime2 = totalCpuTime(devices)
    totalCpuTime3 = (totalCpuTime2 - totalCpuTime1)*cpukel

    cpu = 100 * int(processCpuTime3) / int(totalCpuTime3)
    print(cpu)

# def get_cpu_kel(devices):
#     cmd = "adb -s " +devices +" shell cat /proc/cpuinfo"
#     print(cmd)
#     get_cmd = os.popen(cmd).readlines()
#     print(get_cmd)
#     find_str = "processor"
#     int_cpu = 0
#     for line in get_cmd:
#         if line.find(find_str) >= 0:
#             int_cpu += 1
#     print(int_cpu)
#     return str(int_cpu) + "核"

def top_cpu(devices, pkg_name):
    cmd = "adb -s "+devices+" shell dumpsys cpuinfo | findstr -w " + pkg_name+":"
    print(cmd)
    get_cmd = os.popen(cmd).readlines()
    print(get_cmd)
    for info in get_cmd:
        print(info.split())
        return float(info.split()[2].split("%")[0])

def get_cpu_kel(devices):
    cmd = "adb -s " + devices + " shell cat /proc/cpuinfo"
    print(cmd)
    output = subprocess.check_output(cmd).split()
    sitem = ".".join([x.decode() for x in output])  # 转换为string
    print(len(re.findall("processor", sitem)))
    return len(re.findall("processor", sitem))

if __name__ == "__main__":
    pid = '26767'
    cpu_kel = '8'
    device = '886daa38'
    #
    cpu_rate(pid,cpu_kel,device)
    # get_cpu_kel(device)
    # top_cpu(device,'com.kugou.android.ringtone')
    # get_cpu_kel('886daa38')