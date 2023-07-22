import json
import os

def chunk_data(input_data, max_file_size):
    chunked_data = []
    current_chunk = []
    current_size = 0

    for item in input_data:
        item_size = len(json.dumps(item))
        if current_size + item_size > max_file_size:
            chunked_data.append(current_chunk)
            current_chunk = []
            current_size = 0

        current_chunk.append(item)
        current_size += item_size

    if current_chunk:
        chunked_data.append(current_chunk)

    return chunked_data

def convert_json(input_file, output_folder, max_file_size):
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

    chunked_data = chunk_data(data, max_file_size)

    for idx, chunk in enumerate(chunked_data):
        output_file = os.path.join(output_folder, f"output_{idx + 1}.html")
        with open(output_file, 'w') as json_output_file:
            json.dump(chunk, json_output_file, indent=2)

if __name__ == "__main__":
    input_file = "alpaca_data_cleaned.json"
    output_folder = "output_files"
    max_file_size =  1000 * 999  # <10kB

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    convert_json(input_file, output_folder, max_file_size)
    print(f"Conversion completed. Output saved to {output_folder}.")
