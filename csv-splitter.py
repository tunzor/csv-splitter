import csv
import argparse
import os

parser = argparse.ArgumentParser(description='A csv splitter for sbn')
parser.add_argument('file_name', help="CSV file you want to split")
parser.add_argument('file_record_limit', help="Max number of records in one file", type=int)
args = parser.parse_args()

# Get file name and record limit from command line arguments
file_name = args.file_name
split_file_record_limit = args.file_record_limit

# Extract filename without extension
file_name_no_ext = file_name.split(".")[0]

# Remove any part files previously created
os.system('rm ' + file_name_no_ext + '_part_*')

delimiter = '\n'
file_contents = []
raw_lines_in_file = 0

with open(file_name) as file:
    # Number of lines in the file less the header row
    raw_lines_in_file = sum(1 for row in file) - 1
    print("number of records:", raw_lines_in_file)

    # Reset pointer to beginning of file
    file.seek(0)

    # This creates a csv_data structure from file
    your_file = csv.DictReader(file)

    for line in your_file:
        file_contents.append(line['email'] + delimiter)

    total_record_count = 0
    temp_file_record_count = 0
    file_number = 1

    while total_record_count <= raw_lines_in_file - 1:
        temp_file_name = file_name_no_ext + "_part_" + str(file_number) + ".csv"
        f = open(temp_file_name, "a")
        if temp_file_record_count < split_file_record_limit:
            f.write(file_contents[total_record_count])
            total_record_count += 1
            temp_file_record_count += 1
        else:
            f.close()
            file_number += 1
            temp_file_record_count = 0

    print(str(file_number), "files created")
