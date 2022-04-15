num = int(input())
Prime = True
for i in range(2,num):
    if num % i == 0:
        Prime = False
        break

print(Prime)