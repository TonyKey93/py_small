
def sum_to_char(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum
decypher = []
string_list = []
in_list = input().split()
in_string = input()
for i in in_string:
    string_list.append(i)

exit_list = list(sum_to_char(i) for i in in_list)
while exit_list:
    index = exit_list.pop(0)
    while index > len(string_list):
        index -= len(string_list)
    decypher.append(string_list.pop(index))
print(''.join(decypher))
