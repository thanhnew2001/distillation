import os
import json
import pdfminer
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    try:
        text = extract_text(pdf_path)
        return text
    except pdfminer.pdfminer.exceptions.PDFSyntaxError:
        print(f"Error: Unable to extract text from '{pdf_path}'. The PDF may be scanned or corrupted.")
        return None

def get_text_between_keywords(pdf_text, keyword1, keyword2):
    start_position = pdf_text.find(keyword1)
    if start_position == -1:
        return None

    start_position += len(keyword1)
    end_position = pdf_text.find(keyword2, start_position)
    if end_position == -1:
        return None

    return pdf_text[start_position:end_position]

def process_folder_pdf_files(folder_path, keyword_pairs):
    pdf_objects = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            pdf_text = extract_text_from_pdf(pdf_path)
            if pdf_text:
                pdf_object = {}
                pdf_object['filename'] = filename
                for alt_keywords in keyword_pairs:
                    selected_text = None
                    for keyword_pair in alt_keywords:
                        keyword1, keyword2 = keyword_pair
                        selected_text = get_text_between_keywords(pdf_text, keyword1, keyword2)
                        if selected_text:
                            pdf_object[keyword1] = selected_text.strip()
                            break  # Stop trying alternative keywords if a match is found
                    if selected_text:
                        break  # Stop trying alternative lists of keywords if a match is found
                pdf_objects.append(pdf_object)
    return pdf_objects

# Define the folder path where the PDF files are located
folder_path = 'pdf_files/'

# Define the list of alternative keyword pairs
keyword_pairs = [
    [('TÒA ÁN', 'NHÂN DANH')],
    [('NỘI DUNG VỤ ÁN:', 'NHẬN ĐỊNH CỦA TÒA ÁN:')],
    [('NHẬN ĐỊNH CỦA TÒA ÁN:', 'QUYẾT ĐỊNH:')],
    [('QUYẾT ĐỊNH:', "Nơi nhận:")],

    # Add more alternative keyword pairs here if needed
]

# Process the folder and get PDF objects with selected text between keywords
pdf_objects = process_folder_pdf_files(folder_path, keyword_pairs)

# Write the output data in JSON format
output_file = 'output_data.json'
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(pdf_objects, json_file, ensure_ascii=False, indent=4)

print(f"Data has been written to '{output_file}'.")
