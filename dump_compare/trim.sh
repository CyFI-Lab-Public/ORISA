awk '{
    # Remove the first four fields (nth, paddr, vaddr, len)
    for (i=1; i<=5; i++) { sub(/^[ \t]*[^ \t]*[ \t]+/, ""); }
    type = $1;
    sub(/^[ \t]*[^ \t]+[ \t]*/, "");
    string = $0;
    print type "\t" string;
}' readable.txt > output.txt
