dirty = "./clean.txt"
clean = "/home/cyfi/stuti/fridump/cleaniris/clean.txt"
with open(clean, 'r') as f:
    lines_to_remove = set(f.read().splitlines())

with open(dirty, 'r') as f_in, open('analysis.txt', 'w') as f_out:
    for line in f_in:
        if line.strip() not in lines_to_remove:
            f_out.write(line)
