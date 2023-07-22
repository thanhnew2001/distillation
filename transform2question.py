import json

def convert_to_qa_pairs(json_data):
    qa_pairs = []
    for obj in json_data:
        name = obj["Số:"] if "Số:" in obj else "Unknown"
        for attribute, value in obj.items():
            question = f"{attribute} của bán án {name} là gì?"
            answer = str(value) if value is not None else "N/A"
            qa_pairs.append({"question": question, "answer": answer})
    return qa_pairs

def main():
    input_file = "output_data.json"
    output_file = "qa_pairs.json"

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    qa_pairs = convert_to_qa_pairs(data)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(qa_pairs, f, indent=2, ensure_ascii=False)

    print("Question-Answer pairs have been written to 'qa_pairs.json'.")

if __name__ == "__main__":
    main()
