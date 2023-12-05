with open("input.txt") as file:
    input = file.read().splitlines()

# range_list : list of ranges (start, end)

def get_ranges(mapfile, range_list):

    with open(mapfile) as file:
        input  = file.read().splitlines()

    mapinput = []
    
    for line in input:
        nos = line.split(" ")

        dest = int(nos[0])
        source = int(nos[1])
        trange = int(nos[2])

        # start, end, diff
        mapinput.append((source, source + trange - 1, dest - source))

    mapinput.sort()
    
    mapped_ranges = []

    for to_be_mapped in range_list:

        for i, maprange in enumerate(mapinput):
            
            a = to_be_mapped[0]
            b = to_be_mapped[1]
            c = maprange[0]
            d = maprange[1]

            if(b < c):
                mapped_ranges.append(to_be_mapped)
                break
            elif(a < c and (b >= c and b <= d)):
                mapped_ranges.append([a, c - 1])
                lul = [n + maprange[2] for n in [c, b]]
                mapped_ranges.append(lul)
                break
            elif(a < c and b > d):
                mapped_ranges.append([a, c - 1])
                lul = [n + maprange[2] for n in [c, d]]
                mapped_ranges.append(lul)
                range_list.append([d + 1, b])
                break
            elif((a >= c and a <= d) and b > d):
                lul = [n + maprange[2] for n in [a, d]]
                mapped_ranges.append(lul)
                range_list.append([d + 1, b])
                break
            elif((a >= c and a <= d) and (b <= d and b >= c)):
                lul = [n + maprange[2] for n in [a, b]]
                mapped_ranges.append(lul)
                break
            elif(a > d):
                if(i == len(mapinput) - 1):
                    mapped_ranges.append([a, b])
                else:
                    continue

    return mapped_ranges
    


mapfiles = ["seedsoil.txt", "soilfert.txt", "fertwater.txt", "waterlight.txt", "lighttemp.txt", "temphumid.txt", "humidloc.txt"]

seedline = "seeds: 104847962 3583832 1212568077 114894281 3890048781 333451605 1520059863 217361990 310308287 12785610 3492562455 292968049 1901414562 516150861 2474299950 152867148 3394639029 59690410 862612782 176128197"

seedqueue = seedline.split(" ")

seeds = []

for x in seedqueue:
    if(x.isnumeric()):
        seeds.append(int(x))

seed_rangers = []

for i, seed in enumerate(seeds):
    
    if(i % 2 == 0):
        start_seed = seeds[i]
        runge = seeds[i + 1]

        seed_rangers.append([start_seed, start_seed + runge - 1])

for map in mapfiles:
    
    seed_rangers = get_ranges(map, seed_rangers)

seed_rangers.sort()

print(seed_rangers[0])
