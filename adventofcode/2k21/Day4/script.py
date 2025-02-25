import numpy as np
with open("Day4/input.txt") as f:
    input_lines = f.readlines()

input_lines = [x.strip("\n") for x in input_lines]
sequence = input_lines[0]
input_lines = input_lines[1:]

sequence = [int(x) for x in sequence.split(',')]

input_lines = [x for x in input_lines if x != '']

input_lines = [x.replace("  ", " ") for x in input_lines]
input_lines = [[int(y) for y in x.split(" ") if y != ''] for x in input_lines]

class Board:

    def __init__(self, array):

        self.score = 0
        self.moves = 0

        self.fin_no = 0

        self.rows = []
        self.cols = []

        self.won = False

        for i in range(5):
            self.rows.append(set(array[i]))
        
        for i in range(5):
            self.cols.append(set([array[0][i], array[1][i], array[2][i], array[3][i], array[4][i]]))
        
        self.dict = {}
        for i in range(5):
            for j in range(5):
                self.dict[array[i][j]] = (i, j)
                self.score += array[i][j]

    def play(self, number):
        if(self.won):
            return
        
        self.moves += 1

        if(number not in self.dict.keys()):
            return

        i, j = self.dict[number]

        self.rows[i].remove(number)
        self.cols[j].remove(number)

        self.score -= number

        if(len(self.rows[i]) == 0 or len(self.cols[j]) == 0):
            self.fin_no = number
            self.won = True
    
boards = [Board(input_lines[i * 5 : (i + 1) * 5]) for i in range(100)]

for b in boards:
    for sn in sequence:
        b.play(sn)

print(sorted([(b.moves, b.score * b.fin_no) for b in boards]))