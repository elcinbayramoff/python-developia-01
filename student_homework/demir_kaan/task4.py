
list = [4, 2, 1, 5, 7, 3, 6, 8]
list_sorted = sorted(list)
ae = list_sorted[:2] + list_sorted[2:6][::-1] + list_sorted[6:]
print(ae)

list = [1, 2, 3, 4, 5]
list2 = list[::-1]
print(list2)


