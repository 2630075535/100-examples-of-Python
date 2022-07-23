# 偶数，能够被2整除。


begin = int(input("输入开始值："))
end = int(input("输入结束值："))

def get_even_number(begin, end):
    result = []
    for b in range(begin, end):
        if b % 2 == 0:
            result.append(b)
    return result


print(f"begin = {begin},end = {end}, 之间的偶数为：", get_even_number(begin, end))












