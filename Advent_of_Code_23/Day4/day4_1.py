matches = []

with open("input.txt") as file:
    input = file.read().splitlines()

for line in input:

    l1 = line.split(":")
    l2 = l1[1].split("|")
    winning = l2[0].split(" ")
    mine = l2[1].split(" ")

    true_winning = []
    for win in winning:
        if(win.isnumeric()):
            true_winning.append(win)

    true_mine = []
    for min in mine:
        if(min.isnumeric()):
            true_mine.append(min)

    ans = len(set(true_mine) & set(true_winning))

    matches.append(ans)

final_ans = 0

for match in matches:

    if(match != 0):

        final_ans += (2 ** (match - 1))

print(final_ans)

