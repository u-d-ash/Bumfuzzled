def solve(s):
    no_list = []
    n = len(s)
    #brute force !!!
    for i, char in enumerate(s):
        if(char == 'o'):
            if(i <= n - 3):
                if(s[i + 1] == 'n' and s[i + 2] == 'e'):
                    no_list.append(1)
        elif(char == 't'):
            if(i <= n - 3):
                if(s[i + 1] == 'w' and s[i + 2] == 'o'):
                    no_list.append(2)
            if(i <= n - 5):
                if(s[i + 1] == 'h' and s[i + 2] == 'r' and s[i + 3] == 'e' and s[i + 4] == 'e'):
                    no_list.append(3)
        elif(char == 'f'):
            if(i <= n - 4):
                if(s[i + 1] == 'o' and s[i + 2] == 'u' and s[i + 3] == 'r'):
                    no_list.append(4)
                if(s[i + 1] == 'i' and s[i + 2] == 'v' and s[i + 3] == 'e'):
                    no_list.append(5)
        elif(char == 's'):
            if(i <= n - 3):
                if(s[i + 1] == 'i' and s[i + 2] == 'x'):
                    no_list.append(6)
            
            if(i <= n - 5):
                if(s[i + 1] == 'e' and s[i + 2] == 'v' and s[i + 3] == 'e' and s[i + 4] == 'n'):
                    no_list.append(7)
        
        elif(char == 'e'):
            if(i <= n - 5):
                if(s[i + 1] == 'i' and s[i + 2] == 'g' and s[i + 3] == 'h' and s[i + 4] == 't'):
                    no_list.append(8)
        
        elif(char == 'n'):
            if(i <= n - 4):
                if(s[i + 1] == 'i' and s[i + 2] == 'n' and s[i + 3] == 'e'):
                    no_list.append(9)
        elif(char.isdigit()):
            no_list.append(int(char))

    no_len = len(no_list)

    return (no_list[0] * 10) + no_list[no_len - 1]

final_ans = 0

for i in range(1000):
    x = input()
    final_ans += solve(x)

print(final_ans)

        