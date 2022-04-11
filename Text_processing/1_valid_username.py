import string
def len_test(len_list):
    bigger = [x for x in len_list if len(x) >= 3]
    smaller = [x for x in bigger if len(x) <= 16]
    return smaller

def char_test(char_list):
    flag = 0
    exptected = string.ascii_letters + string.digits + '_' + '-'
    for name in char_list:
        flag = 0
        if 3 > len(name) or len(name) > 16:
            flag = 1
        elif(len([x for x in name if x in exptected])) != len(name):
            flag = 1
        elif flag == 0:
            print(name)
my_list = input().split(', ')
char_test(my_list)
