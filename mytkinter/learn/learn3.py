# -*- coding: utf-8 -*-
import os
import subprocess
import threading
import tkinter as tk # imports
from tkinter import ttk

import yaml

from file_util import get_base_path

# debug日志打印
order = "adb logcat"
line = 'a='
p = subprocess.Popen(order, stdout=subprocess.PIPE, bufsize=1).stdout
for line in iter(p.readline, b''):
    # print(str(line))
    print(str(line.decode()))
