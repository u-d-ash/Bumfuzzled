red_limit = 12
green_limit = 13
blue_limit = 14

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

    THE_VALID = True
    for game in actual_games:
        valid_game = True
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
        
        if(game_jinx[0] > red_limit):
            valid_game = False
        if(game_jinx[1] > green_limit):
            valid_game = False
        if(game_jinx[2] > blue_limit):
            valid_game = False
        
        if(not valid_game):
            THE_VALID = False
            break
    
    if(THE_VALID):
        return int(game_no)
    else:
        return 0


final_ans = 0

for i in range(100):
    s = input()
    final_ans += solve(s)


print(final_ans)