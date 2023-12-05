with open("input.txt") as file:
    input = file.read().splitlines()

def get_val(mapfile, val):

    with open(mapfile) as file:
        input  = file.read().splitlines()
    
    for line in input:
        nos = line.split(" ")

        dest = int(nos[0])
        source = int(nos[1])
        trange = int(nos[2])

        diff = dest - source

        if(val >= source and val <= source + trange - 1):
            return val + diff
    
    return val

mapfiles = ["seedsoil.txt", "soilfert.txt", "fertwater.txt", "waterlight.txt", "lighttemp.txt", "temphumid.txt", "humidloc.txt"]

seedline = "seeds: 104847962 3583832 1212568077 114894281 3890048781 333451605 1520059863 217361990 310308287 12785610 3492562455 292968049 1901414562 516150861 2474299950 152867148 3394639029 59690410 862612782 176128197"

seedqueue = seedline.split(" ")

seeds = []

for x in seedqueue:
    if(x.isnumeric()):
        seeds.append(int(x))

vals = []

for seed in seeds:
    val = seed
    for map in mapfiles:
        val = get_val(map, val)
    
    vals.append(val)

vals.sort()

print(vals[0])