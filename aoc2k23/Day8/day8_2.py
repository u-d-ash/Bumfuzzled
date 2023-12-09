graph = {}
from math import gcd
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

dirx = {'L' : 0, 'R' : 1} 

start_nodes = []

for node in graph:
    if(node[2] == 'A'):
        start_nodes.append(node)

print(start_nodes)

# 6 nodes ending with A

steps = []

for node in start_nodes:
    print(node)
    stop = 0
    index = 0
    while(node[2] != 'Z'):
        index = index % (len(command_string))
        node = graph[node][dirx[command_string[index]]]
        stop += 1
        index += 1
    
    steps.append(stop)

print(steps)

lcm = 1

for lul in steps:
    lcm = (lul * lcm)//gcd(lcm, lul)

print(lcm)




