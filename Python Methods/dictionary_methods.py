my_dict = {"a": 1, "b": 2}
my_dict.keys()           # dict_keys(['a', 'b'])
my_dict.values()         # dict_values([1, 2])
my_dict.items()          # dict_items([('a', 1), ('b', 2)])
my_dict.get("a")         # 1
my_dict.get("c", 0)      # 0 (returns default if key not found)
my_dict.pop("a")         # 1 (removes and returns value for 'a')
my_dict.update({"c": 3}) # {'b': 2, 'c': 3}