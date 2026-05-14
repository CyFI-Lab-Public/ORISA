import re
with open('./readable.txt', 'r') as infile, open('./clean.txt', 'w') as outfile:
    for line in infile:
        res = line.split(' ', -1)
        res = [x for x in res if x.strip()][5:]
        res = ' '.join(str(x) for x in res)
        outfile.write(res)
