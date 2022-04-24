# -*- coding: utf-8 -*-
from mytkinter.PageTab.PageTab1 import *
from mytkinter.PageTab.PageTab11 import init_tab11
from mytkinter.PageTab.PageTab2 import *
from mytkinter.PageTab.PageTab3 import *
from mytkinter.PageTab.PageTab4 import *
from mytkinter.PageTab.PageTab5 import *
from mytkinter.PageTab.PageTab6 import *
from mytkinter.PageTab.PageTab7 import *
from mytkinter.PageTab.PageTab8 import *
from mytkinter.PageTab.PageTab9 import *

win = tk.Tk() # Create instance
win.title("创新测试工具 V2.0.0") # 命名
width = 1200
height = 700

screenwidth = win.winfo_screenwidth()
screenheight = win.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)

win.geometry(alignstr)# 给窗体设置大小
tabControl = ttk.Notebook(win) # Create Tab Control

#-------------------tab1--------------------------------------------------------------------------------------
tab1 = ttk.Frame(tabControl) # Create a tab
tabControl.add(tab1, text='  基础功能  ') # Add the tab
tabControl.pack(expand=1, fill="both") # Pack布局
#对tab1进行布局
init_tab1(tab1)

#-------------------tab2-------------------------------------------------------------------------------------
# tab2 = ttk.Frame(tabControl) # Add a second tab
# tabControl.add(tab2, text=' APP性能测试 ') # Make second tab visible
#
# tabControl.pack(expand=1, fill="both") # Pack布局
# #对tab1进行布局
# init_tab2(tab2)

#-------------------tab9--------------------------------------------------------------------------------------
tab9 = ttk.Frame(tabControl) # Create a tab
tabControl.add(tab9, text=' APP性能手动测试 ') # Add the tab
tabControl.pack(expand=1, fill="both") # Pack布局
# 对tab1进行布局
init_tab9(tab9)

#-------------------tab5----------------------------------
tab5 = ttk.Frame(tabControl) # Add a second tab
tabControl.add(tab5, text=' APP性能自动化测试 ') # Make second tab visible
74890988199235684412
tabControl.pack(expand=1, fill="both") # Pack布局
#对tab1进行布局
init_tab5(tab5)

#-------------------tab6----------------------------------
# tab6 = ttk.Frame(tabControl) # Add a second tab
# tabControl.add(tab6, text=' monkey测试 ') # Make second tab visible
#
# tabControl.pack(expand=1, fill="both") # Pack布局
# #对tab1进行布局
# init_tab6(tab6)

#-------------------tab7--------------------------------------------------------------------------------------
# tab7 = ttk.Frame(tabControl) # Create a tab
# tabControl.add(tab7, text=' 流量测试 ') # Add the tab
# tabControl.pack(expand=1, fill="both") # Pack布局
# #对tab1进行布局
# init_tab7(tab7)

#-------------------tab8--------------------------------------------------------------------------------------
# tab8 = ttk.Frame(tabControl) # Create a tab
# tabControl.add(tab8, text=' 过度绘制 ') # Add the tab
# tabControl.pack(expand=1, fill="both") # Pack布局
# #对tab1进行布局
# init_tab8(tab8)

#-------------------tab9--------------------------------------------------------------------------------------
# tab9 = ttk.Frame(tabControl) # Create a tab
# tabControl.add(tab9, text=' 酷狗铃声UI自动化 ') # Add the tab
# tabControl.pack(expand=1, fill="both") # Pack布局
# # 对tab1进行布局
# init_tab9(tab9)


#-------------------tab4----------------------------------
tab4 = ttk.Frame(tabControl) # Add a second tab
tabControl.add(tab4, text=' 统计测试 ') # Make second tab visible
tabControl.pack(expand=1, fill="both") # Pack布局
#对tab1进行布局
init_tab4(tab4)


# -------------------tab3----------------------------------
# tab3 = ttk.Frame(tabControl) # Add a second tab
# tabControl.add(tab3, text=' 接口测试 ') # Make second tab visible
#
# tabControl.pack(expand=1, fill="both") # Pack布局
# #对tab1进行布局
# init_tab3(tab3)

#-------------------tab11--------------------------------------------------------------------------------------
tab11 = ttk.Frame(tabControl) # Create a tab
tabControl.add(tab11, text=' 酷狗音乐性能指标采集 ') # Add the tab
tabControl.pack(expand=1, fill="both") # Pack布局
#对tab1进行布局
init_tab11(tab11)

win.mainloop() # Start GUI