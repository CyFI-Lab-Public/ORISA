import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python dedupe.py input.txt")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Remove duplicates while preserving order
    seen = set()
    unique_lines = []
    for line in lines:
        if line not in seen:
            seen.add(line)
            unique_lines.append(line)

    # Sort by descending length for priority checking
    sorted_lines = sorted(unique_lines, key=lambda x: -len(x))
    
    kept = []
    for line in sorted_lines:
        # Check if this line is contained in any longer line we've already kept
        if not any(line in kept_line for kept_line in kept):
            kept.append(line)

    # Print results in original file order (but only longest versions)
    final_output = []
    for line in unique_lines:
        if line in kept:
            final_output.append(line)
    
    print('\n'.join(final_output))

if __name__ == "__main__":
    main()
