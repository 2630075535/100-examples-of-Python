"""
import os
for root, dirs, files in os.walk('python/Lib/email'):
    # root代表当前目录
    # dirs代表当前目录下的子目录
    # files代表当前目录下的普通文件

"""

import os

# C:/Users/26300/PycharmProjects/python_study_100
search_dir = "C:/Users/26300/PycharmProjects"
for root, dirs, files in os.walk(search_dir):
    print(root, dirs, files)
