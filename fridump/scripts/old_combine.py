import os
import glob
import r2pipe

# Define the directory where the files are located
dump_directory = "/home/cyfi/stuti/fridump/iris/iris_imm_foreground"

# Get all dump files
all_files = glob.glob(os.path.join(dump_directory, "*.data"))

# Separate files into two categories
dec_files = [f for f in all_files if os.path.basename(f)[0].isdigit()]

# Sort files for better organization
dec_files.sort()

# Define the maximum size for each merged file (1GB = 1073741824 bytes)
MAX_SIZE = 1073741824

def analyze_with_r2(file_path, num, output_report="analysis_report.txt"):
    """Analyze a binary file using radare2 and save results to a report."""
    try:
        # Open the file in radare2
        r2 = r2pipe.open(file_path, flags=['-n', '-w'])  # '-n' for raw binary
        
        # Basic analysis commands
        r2.cmd('e asm.arch=arm') 
        r2.cmd('e asm.bits=64')          
        # Get strings, disassembly, etc.
        strings = r2.cmd('izz')  # Extract strings
        
        print(f"Analysis saved")
        r2.quit()
        with open(f"read{num}.txt", "w") as report:
            report.write(strings)

    except Exception as e:
        print(f"Failed to analyze {file_path}: {e}")


# Function to merge files while keeping each under 1GB
def merge_files(file_list, output_prefix):
    part_num = 1
    output_path = f"{output_prefix}_part{part_num}.data"
    output_file = open(output_path, "wb")
    current_size = 0

    for file in file_list:
        with open(file, "rb") as f:
            data = f.read()
            file_size = len(data)

            # Check if adding this file will exceed 1GB
            if current_size + file_size > MAX_SIZE:
                output_file.close()
                part_num += 1
                output_path = f"{output_prefix}_part{part_num}.data"
                output_file = open(output_path, "wb")
                current_size = 0

            output_file.write(data)
            current_size += file_size

    output_file.close()

# Merge decimal files
merge_files(dec_files, "combined_dec")

# Output merged files
merged_files = glob.glob("combined_*.data")
merged_files

count = 0
for merged_file in merged_files:
    print(f"Analyzing {merged_file}...")
    analyze_with_r2(merged_file, count, f"{merged_file}_analysis.txt")
    count = count + 1

report_files = glob.glob("read*.txt")
report_files.sort()
with open("readable.txt", "w") as combined:
    for report in report_files:
        with open(report, "r") as f:
            combined.write(f.read() + "\n\n")
        os.remove(report)

print("All reports merged into readable.txt")
