# csv-cleaner

Small tool to clean CSV files.

## Usage

    python3 cleaner.py data/sample.csv outputs/clean.csv
Cities are capitalised (lyon -> Lyon).

## Cleaning steps

1. Drop empty rows
2. Strip whitespace in cells
3. Capitalise city names
4. Remove duplicate rows
