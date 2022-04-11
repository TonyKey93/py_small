is_buying = True
items_dict = {}
input_list = []

while is_buying:
    input_data = input()

    if input_data == "buy":
        is_buying = False
        break

    input_list = input_data.split(' ')
    if input_list[0] in items_dict.keys():
        items_dict[input_list[0]] = [float(input_list[1]), float(input_list[2])+int(items_dict[input_list[0]][1])]
    else:
        items_dict[input_list[0]] = [float(input_list[1]), int(input_list[2])]


for k in items_dict:
    total_sum = items_dict[k][0] * items_dict[k][1]
    print(f'{k} -> {total_sum:.2f}')

