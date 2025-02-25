with open("Day1/input.txt") as f:
    input_lines = f.readlines()

values = [int(x) for x in input_lines]

window_vals = [values[i] + values[i + 1] + values[i + 2] for i in range(len(values) - 2)]

count = 0
count2 = 0

for i in range(len(values) - 1):
    count += (values[i + 1] > values[i])

for i in range(len(window_vals) - 1):
    count2 += (window_vals[i + 1] > window_vals[i])

print(count)
print(count2)