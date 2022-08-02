import os

for root,dirs,files in os.walk(r"C:/Users/26300/PycharmProjects"):
    for files in files:
         print(files)