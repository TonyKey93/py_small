def sum_grades(in_dict, i):
    num_grades = len(in_dict[i])
    sum_grades = sum(in_dict[i])
    nok_grades = sum_grades/num_grades
    return nok_grades


n = int(input())
in_list = []
my_dict = {}

for i in range(n):
    name = input()
    grade = float(input())
    if name in my_dict.keys():
        my_dict[name].append(grade)
    else:
        my_dict[name] = [grade]

for i in my_dict.keys():
    final_grade = sum_grades(my_dict, i)
    if final_grade >= 4.50:
        print(f'{i} -> {final_grade:.2f}')
