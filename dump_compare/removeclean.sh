awk 'NR==FNR {a[$0]; next} !($0 in a)' clean.txt testdd1.txt > prompt_unique.txt
