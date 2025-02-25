with open("Day7/input.txt") as f:
    input_line = f.readline()

a = [int(x) for x in input_line.split(",")]

a.sort()
n = len(a)
csum = []

rt = 0

s = 0

for i in range(n):
    rt += a[i]
    s += (a[i] ** 2)
    csum.append(rt)

minf = csum[n - 1] - n * a[0]
posn = a[0]

for i in range(1, n):
    cf = (2 * i - n) * a[i] - 2 * csum[i - 1] + csum[n - 1]
    if(cf < minf):
        minf = cf
        posn = a[i]

print(minf, posn)

minf = s/2 + n/2 * a[0] ** 2 - (csum[n - 1]) * a[0] + 1/2 * (csum[n - 1] - n * a[0])
posn = a[0]

for i in range(1, n):
    cf = s/2 + n/2 * a[i] ** 2 - (csum[n - 1]) * a[i] + 1/2 * ((2 * i - n) * a[i] - 2 * csum[i - 1] + csum[n - 1])
    if(cf < minf):
        minf = cf
        posn = a[i]

print(minf, posn)
