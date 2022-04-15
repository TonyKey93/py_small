my_list = input().split(', ')
zeros_list = list(i for i in my_list if i =='0')
no_zeros_list = list(i for i in my_list if i != '0')
end_list = no_zeros_list + zeros_list
end_list = list(int(i) for i in end_list)

print(end_list)
