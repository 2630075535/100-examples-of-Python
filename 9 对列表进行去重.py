"""
输入，包含重复元素的原始列表：
[10, 20, 30, 10, 20]
返回：
[10, 20, 30]

"""


def get_unique_list(lista):
    result = []
    for item in lista:
        if item not in result:
            result.append(item)
    return result


lista = [10, 20, 30, 10, 12]
print(f"source list {lista}, unique list :", get_unique_list(lista))

# 第二种方法：
print(f"source list {lista}, unique list :", list(set(lista)))


