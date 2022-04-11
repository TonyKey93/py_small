def get_key(my_dict,val):
    for key, value in my_dict.items():
         if val == value:
             return key

def legendary_farming():
    leg_items = {'Shadowmourne': 'shards', 'Valanyr': 'fragments', 'Dragonwrath': 'motes'}
    item_obtained = False
    junk_items_dict = {}
    item_dict = {'shards': 0, 'fragments': 0, 'motes': 0}

    while not item_obtained:
        items= input().lower()
        items = items.split(' ')
        if item_obtained: break
        for value, material in zip(items[0::2], items[1::2]):
            value = int(value)
            material = material.lower()


            if material in ['shards', 'fragments', 'motes']:

                if material not in item_dict:
                    item_dict[material] = value
                else:
                    item_dict[material] += value

            else:
                if material not in junk_items_dict:
                    junk_items_dict[material] = value
                else:
                    junk_items_dict[material] += value

            for item, quantity in item_dict.items():
                if item_dict[item] >= 250:
                    item_dict[item] -= 250
                    item_obtained = True
                    print(f'{get_key(leg_items, item)} obtained!')
                    break
            if item_obtained: break

    for material, quantity in item_dict.items():
        print(f'{material}: {quantity}')
    for material, quantity in junk_items_dict.items():
        print(f'{material}: {quantity}')



legendary_farming()
