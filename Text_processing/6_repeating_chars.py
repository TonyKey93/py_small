my_text = input()
first = my_text[0]
result = [my_text[i] for i in range(len(my_text)) if my_text[i] != my_text[i-1] or i == 0]
new = (''.join(result))
print(new)