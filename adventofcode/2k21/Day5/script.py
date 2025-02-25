with open("Day5/input.txt") as f:
    input_lines = f.readlines()

input_lines = [x.replace(" -> ", ",") for x in input_lines]
input_lines = [x.split(",") for x in input_lines]
input_lines = [[int(y.replace("\n", "")) for y in x] for x in input_lines]

class Line:

    def __init__(self, cords):

        self.x1 = cords[0]
        self.y1 = cords[1]

        self.x2 = cords[2]
        self.y2 = cords[3]
    
    def __repr__(self):
        return f"{self.x1}, {self.y1}, {self.x2}, {self.y2}"

lines = [Line(c) for c in input_lines]

counter_dict = {}

for l in lines:

    if(l.x1 == l.x2):

    
        for i in range(abs(l.y2 - l.y1) + 1):
            if((l.x1, min(l.y1, l.y2) + i) in counter_dict.keys()):
                counter_dict[(l.x1, min(l.y1, l.y2) + i)] += 1
            else:
                counter_dict[(l.x1, min(l.y1, l.y2) + i)] = 1

    
    elif(l.y1 == l.y2):

        for i in range(abs(l.x1 - l.x2) + 1):
            if((min(l.x1, l.x2) + i, l.y1) in counter_dict.keys()):
                counter_dict[(min(l.x1, l.x2) + i, l.y1)] += 1
            else:
                counter_dict[(min(l.x1, l.x2) + i, l.y1)] = 1
    
    elif(abs(l.x1 - l.x2) == abs(l.y1 - l.y2)):

        nos = abs(l.x1 - l.x2) + 1

        if(l.x1 <= l.x2 and l.y1 <= l.y2):
        
            for i in range(nos):
                if((l.x1 + i, l.y1 + i) in counter_dict.keys()):
                    counter_dict[(l.x1 + i, l.y1 + i)] += 1
                else:
                    counter_dict[(l.x1 + i, l.y1 + i)] = 1
        
        elif(l.x1 >= l.x2 and l.y1 >= l.y2):

            for i in range(nos):
                if((l.x1 - i, l.y1 - i) in counter_dict.keys()):
                    counter_dict[(l.x1 - i,l.y1 - i)] += 1
                else:
                    counter_dict[(l.x1 - i, l.y1 - i)] = 1

        elif(l.x1 <= l.x2 and l.y1 >= l.y2):

            for i in range(nos):
                if((l.x1 + i, l.y1 - i) in counter_dict.keys()):
                    counter_dict[(l.x1 + i, l.y1 - i)] += 1
                else:
                    counter_dict[(l.x1 + i, l.y1 - i)] = 1
        
        elif(l.x1 >= l.x2 and l.y1 <= l.y2):

            for i in range(nos):
                if((l.x1 - i, l.y1 + i) in counter_dict.keys()):
                    counter_dict[(l.x1 - i, l.y1 + i)] += 1
                else:
                    counter_dict[(l.x1 - i, l.y1 + i)] = 1

        

count = 0

for i in range(1000):
    for j in range(1000):
        if((i, j) in counter_dict.keys()):
            count += (counter_dict[(i, j)] > 1)

print(count)

