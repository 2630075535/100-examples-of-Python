print("              一、统计文件的大小，KB")
import os
print(os.path.getsize("student_grade_input.txt"))


print("              二、输出目录下的文件名称")
for file in os.listdir("."):
    print(file)


print("              三、输出目录下的文件名称并将目录过滤掉")
for file in os.listdir("."):
    if os.path.isfile(file):
        print(file)

print("              四、输出目录下的所有文件的大小")
sum_size = 0
for file in os.listdir("."):
    if os.path.isfile(file):
        sum_size += os.path.getsize(file)

print("all size of dir:", sum_size/1000)
print(f"all size of dir: {sum_size/1000} KB" )






