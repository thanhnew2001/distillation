import json

def check_json_format(json_list):
    conforming_objects = []
    for obj in json_list:
        if isinstance(obj, dict) and "question" in obj and "answer" in obj:
            conforming_objects.append(obj)
    return conforming_objects

def process_json_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            json_list = json.load(infile)
        conforming_objects = check_json_format(json_list)
        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(conforming_objects, outfile, ensure_ascii=False, indent=4)
        print(f"JSON file '{input_file}' cleaned and saved to '{output_file}'.")
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

# Replace 'input.json' with the path to your JSON file
input_file = 'alpaca_vn.json'
# Replace 'output.json' with the desired output file name
output_file = 'alpaca_vn_cleaned.json'

process_json_file(input_file, output_file)
