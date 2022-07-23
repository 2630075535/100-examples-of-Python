# 计算前n个数字的平方和
a = int(input("请输入所要计算的数字："))
result = 0
while a > 0:
    result = result + a*a

    a -= 1

print("所输入数字的前n项和为：", result)

