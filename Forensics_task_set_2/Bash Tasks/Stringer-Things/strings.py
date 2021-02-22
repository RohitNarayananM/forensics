

with open('test.txt', 'r') as f:
    lines = f.readlines()
for i in range(128,256):
    lines = [line.replace(chr(i), '') for line in lines]
lines = [line.replace(' ', '') for line in lines]
print(lines)
with open('test.txt', 'w') as f:
    f.writelines(lines)