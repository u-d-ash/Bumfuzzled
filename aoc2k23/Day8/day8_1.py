graph = {}

def clean_nodes(s):
    for char in ['=', ',', ')', '(']:
        s = s.replace(char, "")

    s = s.replace(" ", "")
    first = s[:3]
    second = s[3:6]
    third = s[6:]
    graph[first] = (second, third)

with open("input.txt") as file:
    input = file.read().splitlines()



nodes = []

for i, line in enumerate(input):
    if(i == 0):
        command_string = line
    elif(line == ""):
        continue
    else:
        nodes.append(line)

for node in nodes:
    clean_nodes(node)

current_node = 'AAA'
index = 0

dirx = {'L' : 0, 'R' : 1} 
steps = 0
while(current_node != 'ZZZ'):
    print(current_node)
    if(index < len(command_string)):
        current_node = graph[current_node][dirx[command_string[index]]]
        steps += 1
        index += 1
    elif(index == len(command_string)):
        index = 0

print(steps)


