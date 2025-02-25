import random
from tqdm import tqdm

n = 10000000

i = 0

vals = 0

def getrp():
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    return x, y

pbar = tqdm(total=n)

while(i != n):

    x1, y1 = getrp()
    x2, y2 = getrp()

    if(x1 == y1):

        continue

    if(x1 + y1 == 1):

        continue

    if(x1 > y1 and x1 + y1 < 1):

        cord = ((x1 ** 2 + y1 ** 2) - (x2 ** 2 + y2 ** 2))/(2 * (x1 - x2))

        if(cord >= 0 and cord <= 1):

            vals += 1
        
        i += 1
        pbar.update(1)
    
    if(x1 < y1 and x1 + y1 < 1):

        cord = ((x1 ** 2 + y1 ** 2) - (x2 ** 2 + y2 ** 2))/(2 * (y1 - y2))

        if(cord >= 0 and cord <= 1):

            vals += 1
        
        i += 1
        pbar.update(1)
    
    if(x1 < y1 and x1 + y1 > 1):

        cord = ((x1 ** 2 + (y1 - 1) ** 2) - (x2 ** 2 + (y2 - 1) ** 2))/(2 * (x1 - x2))

        if(cord >= 0 and cord <= 1):

            vals += 1

        i += 1
        pbar.update(1)
    
    if(x1 > y1 and x1 + y1 > 1):
    
        cord = (((x1 - 1) ** 2 + y1 ** 2) - ((x2 - 1) ** 2 + y2 ** 2))/(2 * (y1 - y2))

        if(cord >= 0 and cord <= 1):

            vals += 1
        
        i += 1
        pbar.update(1)
    
print(vals/n)

# result : 0.49141198