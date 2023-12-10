
def next_in_line(arr):
    if(len(set(arr)) == 1):
        return arr[0]
    
    last = arr[len(arr) - 1]
    diffs = []
    for i in range(len(arr) - 1):
        diffs.append(arr[i + 1] - arr[i])
    
    return last + next_in_line(diffs)

def previous_in_line(arr):
    if(len(set(arr)) == 1):
        return arr[0]
    
    first = arr[0]

    diffs = []
    for i in range(len(arr) - 1):
        diffs.append(arr[i + 1] - arr[i])

    return first - previous_in_line(diffs)


def solve(line):
    arr = line.split(" ")
    int_arr = [int(n) for n in arr]
    return next_in_line(int_arr), previous_in_line(int_arr)


with open("input.txt") as f:
    input = f.read().splitlines()

answer1 = 0
answer2 = 0
for line in input:
    answer1 += solve(line)[0]
    answer2 += solve(line)[1]

print(answer1)
print(answer2)