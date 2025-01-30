import os
import sys
def remove_duplicate_lines(file_path, line_to_check):

    print(file_path)
    with open(file_path, 'r') as file:
        lines = file.readlines()

    seen = set()
    with open(file_path, 'w') as file:
        for line in lines:
            print(line)
            
            if line.startswith(line_to_check):
                if line_to_check not in seen:
                    #print("line starts with the correct value but has not been seen before")
                    seen.add(line_to_check)
                    file.write(line)

                else:
                    pass #Do nothing, dont write the line 
                    #print("line starts with the correct value AND has been seen before")
            else:
                file.write(line)
    

def process_directory(directory, line_to_check):

    print("checking directory: ", directory)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.par'):
                file_path = os.path.join(root, file)
                remove_duplicate_lines(file_path, line_to_check)

# Directories to process
directories = ['group1', 'group2']

# Line to check for duplicates
line_to_check = 'NE_SW'

# Process each directory
for directory in directories:
    process_directory(directory, line_to_check)