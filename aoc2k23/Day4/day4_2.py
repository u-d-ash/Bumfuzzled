matches = []
card_count = []

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

    card_count.append(1)

    matches.append(ans)

for i, match in enumerate(matches):

    for j in range(match):

        card_count[i + j + 1] += (card_count[i])

print(sum(card_count))



