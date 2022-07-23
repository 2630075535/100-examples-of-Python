"""
简单列表：元素类型不是复合类型（复合类型：列表/元组/字典）
形式1：[20, 50, 10, 40, 30]
形式2：[‘bb’, ‘ee’, ‘aa’, ‘dd’, ‘cc’]

知识点：
怎样原地排序？怎样不改变原列表排序？
怎样指定是升序还是降序排序？

"""

# 原地排序
lista = [20, 40, 30, 50, 10]
lista.sort()
print(f"lista is {lista}")

# 不改变原列表排序
lista = [20, 40, 30, 50, 10]
lista.sort()
listb = sorted(lista)

print(f"lista is {lista}")
print(f"lista is {listb}")

# 倒序1
lista = [20, 40, 30, 50, 10]
# lista.sort()
listb = sorted(lista, reverse = True)

print(f"lista is {lista}")
print(f"lista is {listb}")

# 倒序2
lista = [20, 40, 30, 50, 10]
lista.sort(reverse = True)
# listb = sorted(lista, reverse = True)

print(f"lista is {lista}")
# print(f"lista is {listb}")

