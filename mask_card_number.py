import re

# Function to mask the first 6 digits of a 16-digit number
def mask_number(match):
    number = match.group()
    masked = 'X' * 6 + number[6:]
    return masked

# File paths (you can change them to your specific file paths)
input_file_path = 'input_file.txt'
output_file_path = 'output_file.txt'

# Reading the content from the input file
with open(input_file_path, 'r') as file:
    text = file.read()

# Masking the 16-digit numbers
masked_text = re.sub(r'\b\d{16}\b', mask_number, text)

# Writing the masked content to the output file
with open(output_file_path, 'w') as file:
    file.write(masked_text)

print(f"Masked content saved to {output_file_path}")
