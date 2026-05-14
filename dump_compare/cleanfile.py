import string
import sys

def clean_ascii_file(input_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()
    
    # Decode as ASCII while ignoring non-ASCII characters
    ascii_data = data.decode("ascii", errors="ignore")
    
    # Keep only printable ASCII characters
    cleaned_data = "".join(c for c in ascii_data if c in string.printable)
    
    with open(output_file, "w", encoding="ascii") as f:
        f.write(cleaned_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.txt output.txt")
    else:
        clean_ascii_file(sys.argv[1], sys.argv[2])
