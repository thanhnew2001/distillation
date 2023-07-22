import pdfminer
from pdfminer.high_level import extract_text
import json

def extract_text_from_pdf(pdf_path):
    try:
        text = extract_text(pdf_path)
        return text
    except pdfminer.pdfminer.exceptions.PDFSyntaxError:
        print("Error: Unable to extract text. The PDF may be scanned or corrupted.")
        return None

def text_to_json(text):
    paragraphs = text.split("\n\n")  # Assuming paragraphs are separated by double newlines
    data = {"paragraphs": paragraphs}
    return data

def save_as_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)



# Replace 'your_file.pdf' with the actual path to your PDF file
pdf_path = 'pdf_files/BAN_AN_PT_NGUYEN_THI_HANHNGUYEN_VAN_HAI.pdf'



# Step 1: Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Step 2: Convert to JSON format
json_data = text_to_json(pdf_text)

# Step 3: Save as JSON file
output_file = 'output.json'
save_as_json(json_data, output_file)

print(f"Text content saved to '{output_file}' as JSON.")

