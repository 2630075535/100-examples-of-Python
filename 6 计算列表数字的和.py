def sum_of_list(param_list):
    total = 0
    for item in param_list:
        total += item
    return total


list1 = [1, 2, 33, 4, 5]
list2 = [110, 233, 33, 4, 5]
print(f"sum of {list},", sum_of_list(list1))
print(f"sum of {list},", sum_of_list(list2))


print(f"sum of {list},", sum(list1))
print(f"sum of {list},", sum(list2))

