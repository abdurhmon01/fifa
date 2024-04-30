tuple1 = (('a', 65), ('b', 66), ('c', 67), ('d', 68))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)