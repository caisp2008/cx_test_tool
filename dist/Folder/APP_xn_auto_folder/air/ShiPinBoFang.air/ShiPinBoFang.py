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
    
    
poco(text="发现").click()

poco("com.kugou.shiqutouch:id/pager_rank_smart").swipe([0.0, -0.4105])

poco("android:id/content").child("android.widget.FrameLayout").offspring("com.kugou.shiqutouch:id/fragment_container").offspring("com.kugou.shiqutouch:id/pager_rank_scroll").offspring("com.kugou.shiqutouch:id/pager_rank_content").offspring("com.kugou.shiqutouch:id/list_rank_content").child("com.kugou.shiqutouch:id/list_rank_item")[0].offspring("com.kugou.shiqutouch:id/iv_operation_lookupvideo").click()

poco("android:id/content").child("android.widget.FrameLayout").offspring("com.kugou.shiqutouch:id/ids_short_video_list").child("android.widget.RelativeLayout")[0].child("com.kugou.shiqutouch:id/ids_video_cover").click()


sleep(30)

poco("com.kugou.shiqutouch:id/sv_video_back").click()







