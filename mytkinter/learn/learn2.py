# import tkinter
# from tkinter import ttk # 导入ttk模块，因为下拉菜单控件在ttk中
#
# wuya = tkinter.Tk()
# wuya.title("wuya")
# wuya.geometry("300x200+10+20")
#
#
# # 创建下拉菜单
# cmb = ttk.Combobox(wuya)
# cmb.pack()
# # 设置下拉菜单中的值
# cmb['value'] = ('上海','北京','天津','广州')
#
# # 设置默认值，即默认下拉框中的内容
# cmb.current(2)
# # 默认值中的内容为索引，从0开始
#
# wuya.mainloop()


# from tkinter import *
# root = Tk()
# sb = Scrollbar(root)
# sb.pack(side=RIGHT,fill=Y)
# lb = Listbox(root,yscrollcommand= sb.set)
# for i in range(1000):
#     lb.insert(END,i)
# lb.pack(side=RIGHT)
# sb.config(command=lb.yview)
# mainloop()


import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('111')

# 设置大小和位置,前两个x大小 后两个+位置
win.geometry('400x400+500+200')


def show():
    print(entry.get())


entry = tkinter.Entry(win)

entry.pack()

button = tkinter.Button(win, text='按钮', command=show)

button.pack()

# 进入消息循环
win.mainloop()
