my_list = [1, 2, 3]
my_list.append(4)        # [1, 2, 3, 4]
my_list.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
my_list.insert(0, 0)     # [0, 1, 2, 3, 4, 5, 6]
my_list.remove(3)        # [0, 1, 2, 4, 5, 6] (removes first 3)
my_list.pop()            # 6 (removes and returns last element)
my_list.index(2)         # 2 (index of first 2)
my_list.count(1)         # 1
my_list.sort()           # Sorts list in place
my_list.reverse()        # Reverses list in place