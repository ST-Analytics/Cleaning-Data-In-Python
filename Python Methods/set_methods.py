set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.add(4)              # {1, 2, 3, 4}
set1.remove(1)           # {2, 3, 4}
set1.union(set2)         # {2, 3, 4, 5}
set1.intersection(set2)  # {3, 4}
set1.difference(set2)    # {2}
set1.issubset(set2)      # False
set1.issuperset(set2)    # False