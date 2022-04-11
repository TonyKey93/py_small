my_str = input()
new_str = ''
steps = 0
for idx in range(len(my_str)):
    if my_str[idx] == '>':
        steps += int(my_str[idx+1])
        new_str += '>'

    else:
        if steps == 0:
            new_str += my_str[idx]
        else:
            steps -= 1
print(new_str)



