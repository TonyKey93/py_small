def josephus(ls, skip):
    out_list = []
    idx = 0
    skip -= 1 # pop automatically skips the dead guy
    idx = (idx + skip) % len(ls)
    while len(ls) > 1:
        out_list.append(ls.pop(idx)) # kill prisoner at idx
        idx = (idx + skip) % len(ls)
    out_list.append(ls.pop(0))
    return out_list
my_list = input().split()
skip = int(input())
out_list = josephus(my_list, skip)
out_list = list(int(i) for i in out_list)
out_list = repr(out_list).replace(' ', '')
print(out_list)