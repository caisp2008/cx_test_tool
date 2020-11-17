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
poco("com.kugou.shiqutouch:id/pager_rank_smart").swipe([-0.0959, -0.6061])
poco("com.kugou.shiqutouch:id/list_rank_content").swipe([0.0037, -0.6227])
poco("com.kugou.shiqutouch:id/list_rank_content").swipe([-0.059, -0.6518])
poco("com.kugou.shiqutouch:id/list_rank_content").swipe([-0.0923, -1])
poco("com.kugou.shiqutouch:id/rank_tab_week").click()
poco("com.kugou.shiqutouch:id/list_rank_content").swipe([0.1218, -0.822])
poco("com.kugou.shiqutouch:id/list_rank_content").swipe([-0.1513, -1])

poco("com.kugou.shiqutouch:id/rank_tab_week").click()
poco("com.kugou.shiqutouch:id/list_rank_content").swipe([-0.0738, -0.5833])
poco("com.kugou.shiqutouch:id/list_rank_content").swipe([-0.1107, -0.9112])
poco("com.kugou.shiqutouch:id/list_rank_content").swipe([-0.1033, -1])





