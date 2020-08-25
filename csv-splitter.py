import csv
import argparse
import os

parser = argparse.ArgumentParser(description='A csv splitter for sbn')
parser.add_argument('file_name', help="CSV file you want to split")
parser.add_argument('file_record_limit', help="Max number of records in one file", type=int)
parser.add_argument('--omit', help="Omit emails containing any of these keywords (comma-separated, wrap everything in quotes) e.g. --omit 'word_one, word_two, word_three'", type=str)
args = parser.parse_args()

# Get file name and record limit from command line arguments
file_name = args.file_name
split_file_record_limit = args.file_record_limit

# Extract filename without extension
file_name_no_ext = file_name.split(".")[0]

# Remove any part files previously created
os.system('rm ' + file_name_no_ext + '_part_*')

# Get omission keywords
omission_keywords = []
if args.omit:
    omission_keywords = args.omit.split(",")
    print("Omitting emails containing these words: ", omission_keywords)

delimiter = '\n'
file_contents = []
raw_lines_in_file = 0

with open(file_name) as file:
    # Number of lines in the file less the header row
    raw_lines_in_file = sum(1 for row in file) - 1
    print("number of records:", raw_lines_in_file, "\n")

    # Reset pointer to beginning of file
    file.seek(0)

    # This creates a csv_data structure from file
    your_file = csv.DictReader(file)

    for line in your_file:
        if len(omission_keywords) > 0:
            if not any(keyword in line['email'] for keyword in omission_keywords):
                file_contents.append(line['email'] + delimiter)
        else:
            file_contents.append(line['email'] + delimiter)

    total_record_count = 0
    temp_file_record_count = 0
    file_number = 1

    while total_record_count <= len(file_contents) - 1:
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

    print(str(file_number), "file(s) created")
    print("[Record count] [file name]")
    os.system('wc -l ' + file_name_no_ext + '_part_*')