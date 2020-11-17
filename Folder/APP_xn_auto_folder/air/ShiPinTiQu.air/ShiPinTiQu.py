# -*- encoding=utf8 -*-
__author__ = "liuyi"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

#干掉进程进入APP
shell("am force-stop com.kugou.shiqutouch")

start_app("com.kugou.shiqutouch")

sleep(5)



if(poco("com.kugou.shiqutouch:id/activity_url_hunter_tips_close").exists()):
    poco("com.kugou.shiqutouch:id/activity_url_hunter_tips_close").click()
    
if(poco("com.kugou.shiqutouch:id/iv_dialog_close").exists()):
    poco("com.kugou.shiqutouch:id/iv_dialog_close").click()


    
poco("com.kugou.shiqutouch:id/ids_pager_shiqu_online_extract").click()
poco("com.kugou.shiqutouch:id/ids_pager_online_inputbox").set_text("https://v.douyin.com/ou343g/")
poco("com.kugou.shiqutouch:id/ids_pager_online_start_extract").click()
