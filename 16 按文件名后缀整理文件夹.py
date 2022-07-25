"""
小知识：怎样获取文件的后缀名？
· import os
· os.path.splitext('path/to/aaa.mp3')
  · 输出：('path/to/aaa‘，’.mp3')

小知识：怎样移动文件
· import shutil
· shutil.move("aaa.text","dir/bbb.foo")
"""
print("              一、打印文件夹下的文件名")
import os
dir = "./arrange_dir"

for file in os.listdir(dir):
    print(file)

print("              二、打印文件夹下的文件名")
import os
dir = "./arrange_dir"

for file in os.listdir(dir):
    print(file)

