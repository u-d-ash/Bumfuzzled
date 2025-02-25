with open("Day3/input.txt") as f:
    input_lines = f.readlines()

input_lines = [x.strip("\n") for x in input_lines]

bitcounts = [0] * 12

for inp in input_lines:
    for j in range(12):
        bitcounts[j] += int(inp[j] == '1')

gamma = 0
epsilon = 0

for j in range(12):

    gamma += (bitcounts[j] > 500) * (pow(2, 11 - j))
    epsilon += (bitcounts[j] < 500) * (pow(2, 11 - j))

print(gamma * epsilon)

def convtobin(no):
    count = 0
    for j in range(12):
        count += (no[j] == '1') * (pow(2, 11 - j))
    
    return count

def selectnos(nos, i, code):

    bitnos = [[], []]

    if(len(nos) == 1):
        return nos

    for no in nos:

        if(no[i] == '1'):
            bitnos[1].append(no)
        else:
            bitnos[0].append(no)
        
    if(code == 1):

        if(len(bitnos[1]) >= len(bitnos[0])):
            return bitnos[1]
        else:
            return bitnos[0]

    else:

        if(len(bitnos[0]) <= len(bitnos[1])):
            return bitnos[0]
        else:
            return bitnos[1]

copyone = input_lines.copy()
copytwo = input_lines.copy()

for j in range(12):
    copyone = selectnos(copyone, j, 1)
    copytwo = selectnos(copytwo, j, 0)

print(convtobin(copyone[0]) * convtobin(copytwo[0]))
    
    