import json

def replace_double_quotes_with_single_quotes(data):
    if isinstance(data, dict):
        return {key: replace_double_quotes_with_single_quotes(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [replace_double_quotes_with_single_quotes(item) for item in data]
    elif isinstance(data, str):
        return data.replace('"', "'")
    else:
        return data

def clean_json(input_json):
    # Split the input JSON into separate JSON objects
    json_objects = input_json.strip().split('\n')

    cleaned_json_objects = []
    for json_object in json_objects:
        try:
            # Load the JSON string into a Python object
            data = json.loads(json_object)

            # Apply the replacement function to the data
            cleaned_data = replace_double_quotes_with_single_quotes(data)

            # Convert the cleaned data back to JSON string
            cleaned_json = json.dumps(cleaned_data, ensure_ascii=False, indent=4)

            cleaned_json_objects.append(cleaned_json)
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")

    # Join the cleaned JSON objects and add commas between them to create a valid JSON array
    cleaned_json = ',\n'.join(cleaned_json_objects)

    # Wrap the entire array with square brackets to create a valid JSON array
    cleaned_json = f'[\n{cleaned_json}\n]'

    return cleaned_json

def process_json_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        input_json = infile.read()

    cleaned_json = clean_json(input_json)
    try:
        with open(output_file, 'w', encoding='utf-8', errors='surrogateescape') as outfile:
            outfile.write(cleaned_json)
    except Exception as e:
        print(e)

# Replace 'input.json' with the path to your original JSON file
input_file = 'merged39.json'
# Replace 'output.json' with the desired output file name
output_file = 'merged_cleaned39.json'

process_json_file(input_file, output_file)

print(f"JSON file '{input_file}' cleaned and saved to '{output_file}'.")
