# -*- encoding=utf8 -*-
__author__ = "liuyi"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

#干掉进程进入APP
shell("am force-stop com.kugou.shiqutouch")

start_app("com.kugou.shiqutouch")

poco(text="发现").click()
poco("android:id/content").child("android.widget.FrameLayout").offspring("com.kugou.shiqutouch:id/content_pager").offspring("com.kugou.shiqutouch:id/pager_rank_scroll").offspring("com.kugou.shiqutouch:id/pager_rank_musical").child("android.widget.RelativeLayout")[1].child("com.kugou.shiqutouch:id/musicalcard_bg").click()


touch(Template(r"tpl1591341672616.png", record_pos=(0.326, 0.656), resolution=(1080.0, 1920.0)))



if(poco("com.kugou.shiqutouch:id/guide_pic_call").exists()):
    poco("com.kugou.shiqutouch:id/guide_pic_call").click()

touch(Template(r"tpl1591341914708.png", record_pos=(-0.187, -0.019), resolution=(1080.0, 1920.0)))



sleep(30)
poco("com.kugou.shiqutouch:id/sv_video_back").click()






