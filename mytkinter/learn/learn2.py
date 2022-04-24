
# class MyNumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a +=1
#         return x
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
#
#
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
# myclass  = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x)

# import sys
#
# def fibonacci(n):
#     a,b,counter = 0,1,0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a,b = b,a+b
#         counter +=1
#
# f = fibonacci(10)
#
# while True:
#     try:
#         print(next(f),end=" ")
#     except StopIteration:
#         sys.exit()


# 可写函数说明
# def printinfo(arg1, *vartuple):
# #     "打印任何传入的参数"
# #     print("输出: ")
# #     print(arg1)
# #     print(vartuple)
#
#
# # 调用printinfo 函数
# printinfo(70, 60, 50)
#
#
# # 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
#
#
# # 调用printinfo 函数
# printinfo(10)
# printinfo(70, 60, 50)
# printinfo(10)

# # 可写函数说明
# def printinfo(arg1, **vardict):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vardict)
#
#
# # 调用printinfo 函数
# printinfo(1, a=2, b=3)

# import sys
#
# print('命令行参数如下:')
# for i in sys.argv:
#     print(i)
#
# print('\n\nPython 路径为：', sys.path, '\n')


# #!/usr/bin/python3
# import pickle
#
# # 使用pickle模块将数据对象保存到文件
# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
#
# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)
#
# output = open('data.pkl', 'wb')
#
# # Pickle dictionary using protocol 0.
# pickle.dump(data1, output)
#
# # Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)
#
# output.close()
#
#
# #!/usr/bin/python3
# import pprint, pickle
#
# #使用pickle模块从文件中重构python对象
# pkl_file = open('data.pkl', 'rb')
#
# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)
#
# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)
#
# pkl_file.close()

# import sys
#
# try:
#     f = open('mixsongids.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

#类定义
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性，私有属性再类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print(self.name,self.age,self.__weight)
#
# #实例化类
# p = people('cc',10,50)
# p.speak()

# #类定义
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print(self.name,self.age)
#
# # 单继承例子
# class student(people):
#     grade = ''
#     def __init__(self,n,a,w,g):
#         #调用父类的构函
#         people.__init__(self,n,a,w)
#         self.grade = g
#     #覆写父类的方法
#     def speak(self):
#         print(self.name,self.age,self.grade)
#
#
# #另一个类，多重继承之前的准备
# class speaker():
#     topic = ''
#     name = ''
#     def __init__(self,n,t):
#         self.name = n
#         self.topic = t
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我主题是 %s"%(self.name,self.topic))
#
# #多重继承
# class sample(speaker,student):
#     a = ''
#     def __init__(self,n,a,w,g,t):
#         student.__init__(self,n,a,w,g)
#         speaker.__init__(self,n,t)
#
#
# test = sample('ken',10,30,20,"lallalal")
# test.speak()


#方法重写


# !/usr/bin/python3

# class Parent:  # 定义父类
#     def myMethod(self):
#         print('调用父类方法')
#
# class Child(Parent):  # 定义子类
#     def myMethod(self):
#         print('调用子类方法')
#
#
# c = Child()  # 子类实例
# c.myMethod()  # 子类调用重写方法
# super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法


# class JustCounter:
#     __secretCount = 0 #私有变量
#     publicCount = 0  #公开变量
#
#     def count(self):
#         self.__secretCount +=1
#         self.publicCount +=1
#         print(self.__secretCount)
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)


# import sys
#
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# def outer():
#     num = 10
#     def inner():
#         nonlocal num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()

# import sys
# print(sys.argv)
#
# #二分查找
# def binarySearch(arr, l, r, x):
#     #基本判断
#     if r >=l:
#         mid = int(l+(r-l)/2)
#
#         #元素整好的中间位置
#         if arr[mid]==x:
#             return mid
#
#         elif arr[mid]>x:
#             return binarySearch(arr,1,mid-1,x)
#
#         else:
#             return binarySearch(arr,mid+1,r,x)
#
#     else:
#         return -1


# !/usr/bin/python

# import re
#
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

# import re
#
# result1 = re.findall(r'\d+', 'runoob 123 google 456')
#
# pattern = re.compile(r'\d+')  # 查找数字
# result2 = pattern.findall('runoob 123 google 456')
# result3 = pattern.findall('run88oob123google456', 0, 10)
#
# print(result1)
# print(result2)
# print(result3)

#!/usr/bin/python3

# # CGI处理模块
# import cgi, cgitb
#
# # 创建 FieldStorage 的实例化
# form = cgi.FieldStorage()
#
# # 获取数据
# site_name = form.getvalue('name')
# site_url  = form.getvalue('url')
#
# print ("Content-type:text/html")
# print ()
# print ("<html>")
# print ("<head>")
# print ("<meta charset=\"utf-8\">")
# print ("<title>菜鸟教程 CGI 测试实例</title>")
# print ("</head>")
# print ("<body>")
# print ("<h2>%s官网：%s</h2>" % (site_name, site_url))
# print ("</body>")
# print ("</html>")

# import mysql.connector
# #
# # mydb = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     passwd="123456"
# # )
# #
# # mycursor = mydb.cursor()
# #
# # mycursor.execute("SHOW DATABASES")
# #
# # for x in mycursor:
# #     print(x)

# !/usr/bin/python3
# 文件名：server.py

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    msg = '欢迎访问菜鸟教程！' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()