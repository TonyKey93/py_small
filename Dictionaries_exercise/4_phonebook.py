def phonebook():
    data_dict = {}
    input_data = input()
    is_filled = True
    while is_filled:

        if '-' in input_data:
            data_list = input_data.split('-')

            data_dict[data_list[0]] = data_list[1]
        else:
            my_num = int(input_data)
            is_filled = False
            break
        input_data = input()

    for i in range(my_num):
        name = input()
        if name in data_dict.keys():
            print(f'{name} -> {data_dict[name]}')
        else:
            print(f'Contact {name} does not exist.')



phonebook()