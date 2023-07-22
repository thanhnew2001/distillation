import json

def convert_json(input_file, output_file):
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

    output_data = []
    for item in data:
        question = f"{item['instruction']}"
        if item['input']:
            question += f" - {item['input']}"

        answer = item['output']
        output_data.append({"question": question, "answer": answer})

    with open(output_file, 'w') as json_output_file:
        json.dump(output_data, json_output_file, indent=2)

if __name__ == "__main__":
    input_file = "alpaca_data_cleaned.json"
    output_file = "output.json"
    convert_json(input_file, output_file)
    print(f"Conversion completed. Output saved to {output_file}.")
