import re
in_str = input()
list_re = re.findall(r'\s[A-Za-z]+[-_.]?\w+@[a-z][a-zA-Z.-]*[.][a-z]+', in_str)
for item in list_re:
    print(item)
