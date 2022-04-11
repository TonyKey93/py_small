n = int(input())
plate_dict = {}
for k in range(n):
    data_in = input().split(" ")
    if data_in[0] == "register":
        if data_in[1] in plate_dict.keys():
            print(f'ERROR: already registered with plate number {data_in[2]}')
        else:
            plate_dict[data_in[1]] = data_in[2]
            print(f'{data_in[1]} registered {data_in[2]} successfully')
    elif data_in[0] == "unregister":
        if data_in[1] in plate_dict.keys():
            print(f'{data_in[1]} unregistered successfully')
            plate_dict.pop(data_in[1])
        else:
            print(f'ERROR: user {data_in[1]} not found')

for k in plate_dict.keys():
    print(f'{k} => {plate_dict[k]}')
