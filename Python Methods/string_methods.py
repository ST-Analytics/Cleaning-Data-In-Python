# Basic string methods
"hello".upper()          # HELLO
"WORLD".lower()          # world
"hello world".capitalize() # Hello world
"hello world".title()    # Hello World
"  strip me  ".strip()   # strip me
"hello,world".split(",") # ['hello', 'world']
",".join(["hello", "world"]) # hello,world
"hello".replace("l", "x") # hexxo
"hello".find("l")        # 2 (first occurrence)
"hello".count("l")       # 2
"hello".startswith("he") # True
"hello".endswith("lo")   # True