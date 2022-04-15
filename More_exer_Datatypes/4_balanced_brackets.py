n = int(input())
is_balanced = True
is_opened = False
for i in range(n):
    cmd = input()
    if cmd == '(':
        if is_opened == True:
            break
        is_balanced = False
        is_opened = True
    if cmd == ')':
        if is_opened:
            is_balanced = True
            is_opened = False
        else:
            is_balanced = False
            break
if is_balanced: print("BALANCED")
else: print(f'UNBALANCED')