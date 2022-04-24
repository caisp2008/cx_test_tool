# # -*- encoding=utf-8 -*-
# import os
# import time
# import re
# import sys
# import csv
#
#
# def get_memory(package_name, phone_id=''):
#     phone_name = ''
#     total_mem = ''
#     if phone_id:
#         phone_name = f" -s {phone_id}"
#     cmd = f'adb{phone_name} shell dumpsys meminfo {package_name}'
#     contents = os.popen(cmd).read()
#     if 'TOTAL:' in contents:
#         total_mem = re.findall(r'TOTAL:\s+(\d+)', contents, re.MULTILINE)
#     elif 'TOTAL PSS:' in contents:
#         total_mem = re.findall(r'TOTAL PSS:\s+(\d+)', contents, re.MULTILINE)
#     elif 'com.kugou.android.message' in contents:
#         total_mem = re.findall(r'(\d+\,\d+)K: com.kugou.android \(pid', contents, re.MULTILINE)
#         total_mem = total_mem[3] if len(total_mem) > 4 else total_mem[0]
#         total_mem = ["".join(total_mem.split(','))]
#     if total_mem:
#         result = eval('int(total_mem[0])/1024')
#         return format(result, '.2f')
#     else:
#         return 0
#
#
# def get_devices():
#     cmd = f'adb devices'
#     contents = os.popen(cmd).read()
#     devices_list = re.findall(r'(\w+)\s+device$', contents, re.MULTILINE)
#     return devices_list
#
#
# def get_cpu():
#     pid_front = ['']
#     pid_backend = ['']
#     # 获取pid
#     cmd_ps = 'adb shell ps -ef'
#     cmd_ps_low = 'adb shell ps'
#     try:
#         contents_pid = os.popen(cmd_ps).read()
#         if 'kugou' not in contents_pid:
#             contents_pid = os.popen(cmd_ps_low).read()
#         pid_front = re.findall(r'\s+(\d+).*com\.kugou\.android(?!\.)', contents_pid, re.MULTILINE)
#         pid_backend = re.findall(r'\s+(\d+).*com\.kugou\.android.support', contents_pid, re.MULTILINE)
#         # print(pid_front, pid_backend)
#         # 根据pid筛选前后台进程
#         if pid_front and pid_backend:
#             cmd_top = 'adb shell top -n 1'
#             contents_cpu = os.popen(cmd_top).read()
#             # 前台
#             cpu_front = re.findall(f"{pid_front[0]}.*\w\s(\d+\.\d+).*com\.kugou\.and", contents_cpu, re.MULTILINE)
#             cpu_front = cpu_front if cpu_front else re.findall(f"{pid_front[0]}.*(\d+%).*com\.kugou\.and", contents_cpu,
#                                                                re.MULTILINE)
#             # 后台
#             cpu_backend = re.findall(f"{pid_backend[0]}.*\w\s(\d+\.\d+).*com\.kugou\.and", contents_cpu, re.MULTILINE)
#             cpu_backend = cpu_backend if cpu_backend else re.findall(f"{pid_backend[0]}.*(\d+%).*com\.kugou\.and",
#                                                                      contents_cpu, re.MULTILINE)
#             # print(cpu_front, cpu_backend)
#             return [cpu_front[0] if cpu_front else 0, cpu_backend[0] if cpu_backend else 0]
#         else:
#             return [0, 0]
#     except Exception as e:
#         return [0, 0]
#
#
# if __name__ == "__main__":
#     package_front = "com.kugou.android"  # 前台进程名字
#     package_backend = "com.kugou.android.support"  # 后台进程名字
#     duration = int(sys.argv[1]) if len(sys.argv) > 2 else 10  # 单位：分钟
#     devices = get_devices()  # 获取机型
#     csv_header = ["time", "前台Mem", "后台Mem", "前台CPU", "后台CPU"]
#     print(f"当前机型deviceID：{devices}")
#     with open('kugou_cpu_mem.csv', 'a+') as k:
#         k_csv = csv.writer(k)
#         k_csv.writerow(devices)
#         k_csv.writerow(csv_header)
#     if len(devices) >= 2:
#         print(f"more than one device:{devices}")
#     else:
#         for item in range(duration * 60):
#             record_time = time.strftime('%H:%M:%S', time.localtime())  # 时间
#             mem_data_front = get_memory(package_front)  # 前台进程内存
#             time.sleep(0.5)
#             mem_data_backend = get_memory(package_backend)  # 后台进程内存
#             cpu_data = get_cpu()
#             print(f"time:{record_time}      前台Mem: {mem_data_front}     后台Mem: {mem_data_backend}     "
#                   f"前台CPU: {cpu_data[0]}    后台cpu: {cpu_data[1]}")
#             time.sleep(0.5)
#             with open('kugou_cpu_mem.csv', 'a+', newline='') as k:
#                 k_csv = csv.writer(k)
#                 k_csv.writerow([record_time, mem_data_front, mem_data_backend, cpu_data[0], cpu_data[1]])

a = '425637c0d5f594e70c963142ec77a89c4a51dfaa8aacbfadd2c848eda3cf602d'
b=len(a)
print(b)