import collections

with open("Day8/input.txt") as f:
    input_lines = f.readlines()

input_lines = [x.replace("\n", "") for x in input_lines]
input_lines = [x.split("|") for x in input_lines]
input_lines = [[x[0].split(" "), x[1].split(" ")] for x in input_lines]
input_lines = [[[t for t in x[0] if t != ''], [t for t in x[1] if t != '']] for x in input_lines]
trie_vals = [x[0] for x in input_lines]
out_vals = [x[1] for x in input_lines]

total = 0

for ov in out_vals:
    for w in ov:
        total += (len(w) == 2 or len(w) == 4 or len(w) == 3 or len(w) == 7)

def process_patterns(pats):

    sixlets = []
    fivlets = []

    segment_map = {}

    for w in pats:
        if(len(w) == 2):
            c1 = set([x for x in w])
        elif(len(w) == 7):
            u = set([x for x in w])
        elif(len(w) == 3):
            c7 = set([x for x in w])
        elif(len(w) == 4):
            c4 = set([x for x in w])
        elif(len(w) == 5):
            fivlets.append(set([x for x in w]))
        elif(len(w) == 6):
            sixlets.append(set([x for x in w]))
    
    s1 = c7.difference(c1)
    segment_map[list(s1)[0]] = 1

    allfivs = []
    for f in fivlets:
        allfivs += list(f)
    
    freq = collections.Counter(allfivs)
    sattu = set()
    for k in freq.items():
        if(k[1] == 1):
            sattu.add(k[0])
    
    s2 = sattu.intersection(c4)
    segment_map[list(s2)[0]] = 2
    s5 = sattu.difference(s2)
    segment_map[list(s5)[0]] = 5

    s7 = ((c1.union(c4).union(c7)).intersection(u)).difference(s5)
    segment_map[list(s7)[0]] = 7

    s4 = (fivlets[0].intersection(fivlets[1], fivlets[2])).difference(s1.union(s7))
    segment_map[list(s4)[0]] = 4

    c1l = list(c1)
    x = c1l[0]
    y = c1l[1]
    for f in fivlets:
        if(not (x in f and y in f)):
            if(x in f):
                segment_map[x] = 3
                segment_map[y] = 6
            else:
                segment_map[y] = 3
                segment_map[x] = 6
    
    return segment_map

def get_digit(key, map):
    
    segs = ""

    val = 0

    for c in key:
        segs += str(map[c])
        val += pow(2, map[c] - 1)
    
    print(segs, val)

digmap = {36 : 1, 37 : 7, 102 : }

for tv in trie_vals[0]:
    get_digit(tv, process_patterns(trie_vals[0]))

print(process_patterns(trie_vals[0]))



