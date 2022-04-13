input_str = input()
capital_list = []
for i in range(len(input_str)):
    if input_str[i].isupper():
        capital_list.append(i)
print(capital_list)