import math  # 导入math数学


# 计算圆的半径的函数公式
def computer_area_of_circle(r):
    return round(math.pi * r * r, 2)


print("area of 2 is:", computer_area_of_circle(2))
print("area of 3.14 is:", computer_area_of_circle(3.14))
print("area of 6.78 is:", computer_area_of_circle(6.78))
print("area of 9 is:", computer_area_of_circle(9))
