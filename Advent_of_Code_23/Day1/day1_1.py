def solve(s):
    no_list = []
    for char in s:
        if(char.isdigit()):
            no_list.append(int(char))
    
    n = len(no_list)
    return (10 * no_list[0]) + no_list[n - 1]

final_ans = 0

for i in range(1000):
    x = input()
    final_ans += solve(x)

print(final_ans)