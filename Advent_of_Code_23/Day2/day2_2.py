
def solve(s):
    split_one = s.split(":")
    game_no = split_one[0].split(" ")[1]
    sequences = split_one[1].split(";")
    actual_games = []
    for seq in sequences:
        stripped_game = []
        for game in seq.split(","):
            stripped_game.append(game.replace(" ", ""))

        actual_games.append(stripped_game)
    gamejinxes = []
    for game in actual_games:
        game_jinx = [0, 0, 0]
        for roll in game:
            no = []
            color = []
            for char in roll:
                if(char.isdigit()):
                    no.append(char)
                else:
                    color.append(char)
            len_no = len(no)
            act_no = 0
            for i, x in enumerate(no):
                act_no += (int(x) * (10 ** (len_no - 1 - i)))
            
            if(color[0] == 'r'):
                game_jinx[0] = act_no
            elif(color[0] == 'g'):
                game_jinx[1] = act_no
            elif(color[0] == 'b'):
                game_jinx[2] = act_no
        
        gamejinxes.append(game_jinx)
    
    blue_min = 0
    red_min = 0
    green_min = 0
    for jinx in gamejinxes:
        green_min = max(green_min, jinx[1])
        blue_min = max(blue_min, jinx[2])
        red_min = max(red_min, jinx[0])
    
    return blue_min * red_min * green_min


final_ans = 0
for i in range(100):
    
    s = input()
    final_ans += solve(s)


print(final_ans)