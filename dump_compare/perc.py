import sys
import re

def read_y_words(y_file):
    """Read words from Y file into a set for O(1) lookups."""
    with open(y_file, 'r') as f:
        #print(f.read().split())
        return set(f.read().split())
        #return set(word.lower() for line in f for word in re.findall(r'\b\w+\b', line))

def count_common_words(x_file, y_words):
    """Count how many Y words are present in X file."""
    with open(x_file, 'r') as f:
        content = f.read().lower()  # Case-insensitive comparison
        x_words = set(re.findall(r'\b\w+\b', content))  # Split into words
    return len(y_words & x_words)

def main():
    if len(sys.argv) < 3:
        print("Usage: python word_counter.py <y_file> <x_files...>")
        sys.exit(1)
    
    y_file = sys.argv[1]
    x_files = sys.argv[2:]
    
    y_words = read_y_words(y_file)
    
    for x_file in x_files:
        count = count_common_words(x_file, y_words)
        print(f"{x_file}: {count}")

    print(y_words)
    print(len(y_words))
if __name__ == "__main__":
    main()
