#!/bin/bash

read -p "Enter the path to the readable file: " input_path

# Check if file exists
if [ ! -f "$input_path" ]; then
    echo "Error: File $input_path not found!"
    exit 1
fi

# Generate output path in the same directory
output_dir=$(dirname "$input_path")
output_path="$output_dir/trimmed_readable.txt"

awk '{
    # Remove the first four fields (nth, paddr, vaddr, len)
    for (i=1; i<=5; i++) { sub(/^[ \t][^ \t][ \t]+/, ""); }
    type = $1;
    sub(/^[ \t][^ \t]+[ \t]/, "");
    string = $0;
    print type "\t" string;
}' "$input_path" > "$output_path"

echo "Output saved to: $output_path"
