def diagonals(array):
    if array[0][0] == array[1][1] == array[2][2] and array[0][0]:
        return array[0][0]
    elif array[0][2] == array[1][1] and array[2][0] and array[0][0]:
        return array[0][2]
    else: return 0

def rows(array):
    no_winner = False
    for i in range(3):
        if array[i][0] == array[i][1] == array[i][2] and array[i][0]:
            return array[i][0]
        else: no_winner = True
    if no_winner: return 0

def columns(array):
    no_winner = False
    for i in range(3):
        if array[0][i] == array[1][i] == array[2][i] and array[0][i]:
            return array[0][i]
        else: no_winner = True
    if no_winner: return 0

row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
array = [row1,row2,row3]
winner = max(columns(array),rows(array), diagonals(array))
if winner == 1:
    print('First player won')
elif winner == 2:
    print('Second player won')
elif winner == 0:
    print('Draw!')
