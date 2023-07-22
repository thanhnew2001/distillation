import json

def filter_and_copy_objects(json_data, property_name):
    filtered_data = [obj for obj in json_data if property_name in obj]
    return filtered_data

def main():
    input_file = "output_data.json"
    output_file = "filtered_data.json"
    property_name = "Số:"

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    filtered_data = filter_and_copy_objects(data, property_name)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(filtered_data, f, indent=2, ensure_ascii=False)

    print("Filtered data (objects with the '{}' property) has been written to 'filtered_data.json'.".format(property_name))

if __name__ == "__main__":
    main()
