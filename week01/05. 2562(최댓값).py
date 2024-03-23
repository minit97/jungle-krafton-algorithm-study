_list = []
for i in range(9):
    _list.append(int(input()))

max_value = max(_list)
print(max_value)
print(_list.index(max_value) + 1)