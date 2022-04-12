import re
my_str = input()
txt = re.findall(r"\b(_)[a-zA-Z0-9]+", my_str)
print(",".join(txt))