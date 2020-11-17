# -*- encoding=utf8 -*-
__author__ = "liuyi"

from airtest.core.api import *
from poco.drivers.cocosjs import CocosJsPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

#干掉进程进入APP
shell("pm clear com.kugou.shiqutouch")

#冷启动app
start_app("com.kugou.shiqutouch")

#首次启动，同意协议

poco("com.kugou.shiqutouch:id/apply_permission_ok").click()

if(poco("com.kugou.shiqutouch:id/apply_permission_ok").exists()):
    poco("com.kugou.shiqutouch:id/apply_permission_ok").click()


sleep(5)

poco("com.kugou.shiqutouch:id/iv_dialog_close").click()


















