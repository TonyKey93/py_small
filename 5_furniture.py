import re
price = 0.0
quantity = 0
spent_money = 0
pattern = '>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
furniture_list = []
is_buying = True

while is_buying:
    data = input()
    if data == "Purchase":
        is_buying = False
        break
    result = re.match(pattern, data)
    if result is not None:
        spent_money += float(result[2])*int(result[3])
        furniture_list.append(result[1])

print(f'Bought furniture:')
for item in furniture_list:
    print(item)
print(f'Total money spend: {spent_money:.2f}')