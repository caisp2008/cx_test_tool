
# list = []
# with open("D:\CC\program\cx_test_tool\mytkinter\learn\mixsongids.txt", "r") as f:  # 打开文件
#
#     for i in range(301):
#         a = f.readline().strip()
#         # print(a)
#         list.append(int(a))
# print(list)


list = []

i=1
for i in range(51):
        list.append("{\"" + "label\":\"更改后" + str(i+1) + "\" ,\"lid\":" + str(i+1)+"}")
        print('[' + ', '.join(list) + ']')


# print(list)