
with open("Day2/input.txt") as f:
    input_lines = f.readlines()

input_lines = [x.split() for x in input_lines]

x = 0
y = 0

for inp in input_lines:
    if(inp[0] == 'forward'):
        x += int(inp[1])
    elif(inp[0] == 'up'):
        y -= int(inp[1])
    else:
        y += int(inp[1])
    
print(x * y)

x = 0
y = 0
aim = 0

for inp in input_lines:
    if(inp[0] == 'forward'):
        x += int(inp[1])
        y += aim * int(inp[1])
    elif(inp[0] == 'up'):
        aim -= int(inp[1])
    else:
        aim += int(inp[1])

print(x * y)