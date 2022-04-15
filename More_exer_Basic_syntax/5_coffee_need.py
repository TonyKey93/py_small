import re
is_finished = False
cmd = input()
regex = r'coding|dog|cat|movie'
counter = 0
double = False

while cmd != "END":
    if cmd.isupper():
        double = True

    result = re.match(regex,cmd, re.IGNORECASE)
    if result is not None:
        if double: counter += 2
        else: counter += 1

    cmd = input()
    double = False
if counter > 5:
    print("You need extra sleep")
else: print(counter)