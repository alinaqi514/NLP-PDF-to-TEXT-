import csv

# Specify the path or name of your text file
text_file_path = 'PatientReport.txt'

# Read the content of the text file
with open(text_file_path, 'r') as file:
    text_content = file.read()

# Split the content into lines
lines = text_content.split('\n')

# Create a dictionary from the lines
my_dict = {}
for line in lines:
    # Check if the line contains a colon
    if ':' in line:
        # Split the line into key and value
        key, value = map(str.strip, line.split(':', 1))
        my_dict[key] = value

# Specify the CSV file name
csv_file_name = 'output_data2.csv'

# Write the dictionary to a CSV file
with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Key', 'Value'])  # Write header
    csv_writer.writerows(my_dict.items())  # Write key-value pairs

print(f'Dictionary has been written to {csv_file_name}')
