import pandas as pd



input_filename = "backend/fakeapi/products.csv"
output_filename = "backend/fakeapi/products_clean.csv"

with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    for line in infile:
        # Remove the first two commas and write the line to the output file
        new_line = line.lstrip(',')
        if new_line.startswith(','):
            new_line = new_line[1:]
        outfile.write(new_line)
