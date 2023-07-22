import os
import json
from docx import Document

def split_json(json_path, output_dir, max_file_size=300000):
    # Read the JSON file
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # Serialize the JSON data into a list of strings
    json_strings = [json.dumps(item) for item in data]

    # Initialize variables
    current_file_size = 0
    current_file_index = 0
    current_file_data = []

    # Split the JSON strings into smaller files
    for json_string in json_strings:
        json_string_size = len(json_string)
        if current_file_size + json_string_size > max_file_size:
            write_file(output_dir, current_file_index, current_file_data)
            current_file_data = []
            current_file_index += 1
            current_file_size = 0

        current_file_data.append(json_string)
        current_file_size += json_string_size
    
    # Write the last batch of data to the last file
    if current_file_data:
        write_file(output_dir, current_file_index, current_file_data)

def write_file(output_dir, index, data):
    file_path = os.path.join(output_dir, f'output_{index}.docx')
    doc = Document()
    for item in data:
        doc.add_paragraph(item)
    doc.save(file_path)

if __name__ == "__main__":
    # Specify the input JSON file path and output directory
    input_json_path = 'output.json'
    output_directory = 'output_folder'

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Split the JSON file into smaller DOCX files
    split_json(input_json_path, output_directory)
