#Sum of a Beach
#
#Beaches are filled with sand, water, fish, and sun.
#Given a string, calculate how many times the words
#"Sand", "Water", "Fish", and "Sun" appear (case insensitive).

import re

regex = r'water|fish|sand|sun'
my_string = input().lower()
result = re.findall(regex,my_string)
print(len(result))
