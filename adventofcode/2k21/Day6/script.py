with open("Day6/input.txt") as f:
    input_lines = f.readline()

vals = [int(x) for x in input_lines.split(",")]

f = [0] * 7

for i in range(7, 300):
    v = 1 + f[i - 7]
    if(i - 9 >= 0):
        v += f[i - 9]
    f.append(v)

def solve(t, x):
    if(t <= x):
        return 1
    
    answer = f[t - x - 1]
    if(t - x - 3 >= 0):
        answer += f[t - x - 3]
    
    return answer

fina = 0

for v in vals:
    fina += solve(256, v)

print(fina + 2 * len(vals))
