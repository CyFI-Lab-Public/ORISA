import re

def is_vector_like(line, min_numbers=10):
    # Match floats (e.g., 1.23, -0.456, 2.0e-3, etc.)
    numbers = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    return len(numbers) >= min_numbers

file_path = 'iris_bg_imm.txt'  # Replace with your file path

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        if is_vector_like(line):
            print(f"[Line {i+1}] Possible vector: {line.strip()}")
