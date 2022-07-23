# 原始列表
lista = [3, 5, 7, 9, 11, 13]
listb = [7, 9, 11]


def remove_elements_from_list(lista, listb):
    for item in listb:
        lista.remove(item)
    return lista


print(f"from{lista} remove {listb}, result:", remove_elements_from_list(lista, listb))


# 方法二：
lista = [3, 5, 7, 9, 11, 13]
listb = [7, 9, 11]
data = [item for item in lista if item not in listb]
print(f"from{lista} remove {listb}, result:", data)


