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
poco("com.kugou.shiqutouch:id/pager_rank_smart").swipe([0.0739, -0.8249])
poco("com.kugou.shiqutouch:id/pager_rank_smart").swipe([0.0739, -0.8249])
poco("com.kugou.shiqutouch:id/pager_rank_smart").swipe([0.0739, -0.8249])
poco("com.kugou.shiqutouch:id/pager_rank_smart").swipe([0.0739, -0.8249])

poco("com.kugou.shiqutouch:id/rank_tab_week").click()


poco(text="Love is gone (Justin Dai & Marvin Bootleg) (Marvin remix)").swipe([0.1907, -0.784])

poco("com.kugou.shiqutouch:id/list_rank_content").swipe([0.1751, -1])

poco("com.kugou.shiqutouch:id/list_rank_content").swipe([0.1751, -1])