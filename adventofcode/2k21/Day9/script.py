with open("Day9/input.txt") as f:
    input_lines = f.readlines()

input_lines = [x.replace("\n", "") for x in input_lines]
array = [[int(x) for x in y] for y in input_lines]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

score = 0

for i in range(100):
    for j in range(100):

        risk = True

        for k in range(4):

            nx = i + dx[k]
            ny = j + dy[k]

            if(nx >= 0 and nx < 100 and ny >= 0 and ny < 100):

                if(array[nx][ny] <= array[i][j]):
                    risk = False
                    break
        
        if(risk):
            score += (array[i][j] + 1)

print(score)

# I hate python so bad !!! :(