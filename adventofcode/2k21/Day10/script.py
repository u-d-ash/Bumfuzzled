with open("Day10/input.txt") as f:
    input_lines = f.readlines()

input_lines = [x.replace("\n", "") for x in input_lines]

def get_score(line):
    stack = []
    for char in line:
        if(char == '{' or char == '(' or char == '[' or char == '<'):
            stack.append(char)
        else:
            last_one = stack[-1]
            if(char == '}'):
                if(last_one == '{'):
                    stack.pop()
                else:
                    return (1, 1197)
            elif(char == ')'):
                if(last_one == '('):
                    stack.pop()
                else:
                    return (1, 3)
            elif(char == '>'):
                if(last_one == '<'):
                    stack.pop()
                else:
                    return (1, 25137)
            else:
                if(last_one == '['):
                    stack.pop()
                else:
                    return (1, 57)

    s = 0
    sd = {'(' : 1, '[' : 2, '{' : 3, '<' : 4}
    stack.reverse()
    for char in stack:
        s = 5 * s
        s += sd[char]
    
    return (2, s)

score1 = 0
score2s = []

for line in input_lines:
    a, b = get_score(line)
    score1 += (a == 1) * (b)
    if(a == 2):
        score2s.append(b)

score2s.sort()

print(score1)
print(score2s[int((len(score2s) - 1)/2)])




                