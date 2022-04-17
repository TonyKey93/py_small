def time_sum(my_list):
    sum_all = 0
    for i in my_list:
        sum_all += i
        if i == 0:
            sum_all *= 0.8
    return sum_all


in_list = input().split()
in_list = list(int(i) for i in in_list)
mid_index = len(in_list)//2
first_list = in_list[:mid_index]
second_list = in_list[mid_index+1:]
first_car = time_sum(first_list)
second_car = time_sum(second_list)
if first_car < second_car:
    print(f'The winner is left with total time: {first_car:.1f}')
elif first_car > second_car:
    print(f'The winner is right with total time: {second_car:.1f}')
else:
    pass