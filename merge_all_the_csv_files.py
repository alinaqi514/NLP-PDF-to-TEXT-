import os
import glob
import csv

# Specify the directory where your CSV files are located
csv_files_path = r'C:\Users\bauss\Desktop\Open CV'  # Change this to the actual path of your CSV files

# Create a list to store data from all CSV files
all_data = []

# Iterate through each CSV file in the directory
for csv_file in glob.glob(os.path.join(csv_files_path, 'Page_*_output.csv')):
    try:
        # Read data from each CSV file
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                all_data.append(row)
    except Exception as e:
        print(f"Error reading data from {csv_file}: {e}")

# Write the combined data to a new CSV file
output_csv_file = 'AllData.csv'
try:
    # Determine fieldnames dynamically based on keys in the data
    fieldnames = set()
    for row in all_data:
        fieldnames.update(row.keys())

    with open(output_csv_file, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=list(fieldnames))
        writer.writeheader()
        writer.writerows(all_data)

    print(f"All data successfully written to {output_csv_file}")
except Exception as e:
    print(f"Error writing data to {output_csv_file}: {e}")
