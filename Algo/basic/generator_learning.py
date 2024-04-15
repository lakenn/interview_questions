import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            yield row

def process_data(rows):
    for row in rows:
        # Perform some processing on the row
        yield row

def write_csv(rows, output_path):
    with open(output_path, 'w') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)

input_file = "large.txt"
output_file = "processed_data.csv"

rows = read_csv(input_file)
processed_rows = process_data(rows)
write_csv(processed_rows, output_file)