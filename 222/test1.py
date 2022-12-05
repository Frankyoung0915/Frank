import copy
list_1 = [1,2,3]
list_2 = [list_1]
list_3 = copy.copy(list_2)
list_4 = copy.deepcopy(list_2)

print(list_1 is list_2[0])
print(list_1 is list_3[0])
print(list_1 is list_4)
print(list_2[0] is list_3[0])
print(list_2 is list_4)
