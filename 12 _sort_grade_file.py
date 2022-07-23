"""
输入文件：
  三列：学号、姓名、成绩
  列之间用逗号分割，比如”101，小张，88“
  行之间用\n换行分割
处理：
  读取文件，按成绩倒序排列

输出：
  排序后的三列数据
"""


def read_file():
    result = []
    with open("student_grade_input.txt") as fin:
        for line in fin:
            line = line[:-1]
            result.append(line.split(","))
    return result


def sort_grade(datas):
    return sorted(datas, key=lambda x: int(x[2]), reverse=True)


def write_file(datas):
    with open("student_grade_input.txt", "w") as fout:
        for data in datas:
            fout.write(",".join(data) + "\n")


# 读取数据文件
datas = read_file()
print("read_file datas:", datas)
# 排序数据
datas = sort_grade(datas)
print("sort_grades datas:", datas)
# 写出文件
write_file(datas)



