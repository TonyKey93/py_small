import re
data = input()
item = input()
pattern = rf'\b{item}\b'
data_list = re.findall(pattern, data, re.IGNORECASE)
print(len(data_list))