import re
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
txt = re.findall("\d+", text)
print(' '.join(txt))