my_list = input().split(' ')
sorted_list = sorted(my_list, key=len)
med_result = 0
end_sum = 0

for i in range(len(sorted_list[0])):
    med_result = ord(sorted_list[0][i]) * ord(sorted_list[1][i])
    end_sum += med_result

left_ord = len(sorted_list[1]) - len(sorted_list[0])
if left_ord != 0:
    num_left = len(sorted_list[1]) - left_ord
    all_len = len(sorted_list[1])

    for i in range(num_left, all_len):
        end_sum += ord(sorted_list[1][i])

print(end_sum)