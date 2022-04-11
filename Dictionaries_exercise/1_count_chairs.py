from collections import Counter

my_dict = {}
my_str = input()
my_dict = Counter(my_str)
my_dict.pop(' ')
for key, value in my_dict.items():
    print(f'{key} -> {value}')