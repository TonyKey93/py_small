my_string = input()
new_string = ''
for i in range(len(my_string)):
    new_string += chr(ord(my_string[i]) + 3)
print(new_string)
