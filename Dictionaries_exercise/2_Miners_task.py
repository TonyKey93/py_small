def miner_task():
    resurs_dict = {}
    is_running = True
    resurs = input()

    while is_running:
        quantity = input()
        quantity = int(quantity)
        if resurs not in resurs_dict.keys():
            resurs_dict[resurs] = quantity
        else:
            resurs_dict[resurs] += quantity
        resurs = input()
        if resurs == "stop":
            is_running = False
            break

    for key, value in resurs_dict.items():
        print(f'{key} -> {value}')

miner_task()