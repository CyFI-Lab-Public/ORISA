Java.perform(function() {
    var file = new File("/sdcard/memory_dump.bin", "wb");
    var ranges = Process.enumerateRanges('r--');
    
    ranges.forEach(function(range) {
        var memDump = Memory.readByteArray(range.base, range.size);
        file.write(memDump);
    });

    file.close();
    console.log("Memory dumped to /sdcard/memory_dump.bin");
});