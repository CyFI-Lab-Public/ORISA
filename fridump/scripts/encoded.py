def is_vector_line(line):
    try:
        numbers = list(map(float, line.strip().replace(',', ' ').replace('[','').replace(']','').split()))
        return len(numbers)
    except ValueError:
        return 0

with open('iris_bg_imm.txt', 'r') as f:
    lines = f.readlines()

vector_lengths = [is_vector_line(line) for line in lines]
non_zero = [l for l in vector_lengths if l > 0]

if non_zero and all(l == non_zero[0] for l in non_zero):
    print(f"File looks like embeddings. Each line has {non_zero[0]} dimensions.")
else:
    print("File is not consistent or may not be embeddings.")
