is_running = True
comp_dict = {}

while is_running:
    data_in = input()
    if data_in == "End":
        is_running = False
        break
    data_list = data_in.split(' -> ')
    key = data_list[0]
    id = data_list[1]
    if key in comp_dict.keys():
        if id in comp_dict[key]:
            pass
        else:
            comp_dict[key].append(id)
    else:
        comp_dict[key] = [id]

for key in comp_dict.keys():
    print(key)
    for name in comp_dict[key]:
        print(f'-- {name}')