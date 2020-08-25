# CSV Splitter
This command line app is used to split a `csv` file containing email addresses and other data into smaller part files containing just the email addresses for use in automated mailing services like [SurveyMonkey](https://www.surveymonkey.com/).

> NOTE: The source `csv` file must have a header row with at least `email` as a column name

## Features
- Maximum number of email addresses in outputted part files is configurable
- Automatically determines and creates as many part files as required
- Can be used on different source files in the same directory as outputted part filenames use the source filename
- Automatically removes part files created from previous runs before running again (only part files containing source filename; part files from other source files are untouched)
    - Running with source `file1.csv` would remove `file1_part_*` files but not `file2_part_*` files

## Usage
Two positional arguments are required: **the source file** to split and the **maximum number of records** in the part file.

`python csv-splitter.py file_name.csv 999`

Optionally a list of keywords can be provided and any email address containing *any* of the keywords will be omitted.

`python csv-splitter.py file_name.csv 999 --omit "google, yahoo, james"`

The part files are named after the source file and suffixed with `_part_` and the part file number.

## Example
Source file `customers.csv` with 14580 records (+ header row) and max records config of `2000`:

`python csv-splitter.py customers.csv 2000`

`8` part files would be created:
```
# 2000 records each
customers_part_1.csv
customers_part_2.csv
customers_part_3.csv
customers_part_4.csv
customers_part_5.csv
customers_part_6.csv
customers_part_7.csv

# 580 records
customers_part_8.csv
```
