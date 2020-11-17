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

poco(text="发现").click()



#可能会弹出推送通知弹窗
if(poco("com.kugou.shiqutouch:id/iv_dialog_firstLine").exists()):
    poco("com.kugou.shiqutouch:id/iv_dialog_close").click()
    
    
poco("com.kugou.shiqutouch:id/pager_rank_smart").swipe([0.0078, -0.3716])

    
poco("android:id/content").child("android.widget.FrameLayout").offspring("com.kugou.shiqutouch:id/fragment_container").offspring("com.kugou.shiqutouch:id/pager_rank_scroll").offspring("com.kugou.shiqutouch:id/pager_rank_content").offspring("com.kugou.shiqutouch:id/list_rank_content").child("com.kugou.shiqutouch:id/list_rank_item")[0].child("com.kugou.shiqutouch:id/iv_play_status").click()


poco("com.kugou.shiqutouch:id/display_live_scroll").click()

poco("com.kugou.shiqutouch:id/iv_play_status").click()

#可能会出现滑动引导
if(poco("com.kugou.shiqutouch:id/pager_song_display_anim").exists()):
    poco("com.kugou.shiqutouch:id/pager_song_display_anim").click()
    poco("com.kugou.shiqutouch:id/pager_song_display_anim").click()
    



#在播放页听歌30秒
sleep(30)







