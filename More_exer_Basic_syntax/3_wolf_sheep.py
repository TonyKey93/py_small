herd = input().split(', ')
for i in herd:
    if i == "wolf":
        wolf_index = herd.index(i)
        if wolf_index == len(herd)-1:
            print('Please go away and stop eating my sheep')
        else:
            sheep_num = len(herd)-wolf_index-1
            print(f'Oi! Sheep number {sheep_num}! You are about to be eaten by a wolf!')
