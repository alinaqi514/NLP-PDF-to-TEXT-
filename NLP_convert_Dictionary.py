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

print(my_dict)
