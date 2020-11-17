# -*- encoding=utf8 -*-
__author__ = "liuyi"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

#干掉进程进入APP
shell("am force-stop com.kugou.shiqutouch")
start_app("com.kugou.shiqutouch")
sleep(4)

poco("android.widget.FrameLayout").offspring("com.kugou.shiqutouch:id/common_tab_layout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout")[3].offspring("com.kugou.shiqutouch:id/iv_tab_icon").click()

if(poco("com.kugou.fanxing.allinone.sdk:id/privacy_notice_dialog_agree").exists()):
    poco("com.kugou.fanxing.allinone.sdk:id/privacy_notice_dialog_agree").click()


poco("android:id/content").offspring("com.kugou.fanxing.allinone.sdk:id/tab_viewpager").offspring("com.kugou.fanxing.allinone.sdk:id/fa_recyclerview").child("android.widget.RelativeLayout")[0].offspring("com.kugou.fanxing.allinone.sdk:id/live_user_image").click()

sleep(10)


poco("com.kugou.fanxing.allinone.sdk:id/fa_patpat_guide_content").click()

sleep(30)

poco("com.kugou.fanxing.allinone.sdk:id/fa_layout_hide_top_close").click()

poco("com.kugou.fanxing.allinone.sdk:id/fa_first_exit_guide_hint").click()

poco("com.kugou.fanxing.allinone.sdk:id/fa_layout_hide_top_close").click()


