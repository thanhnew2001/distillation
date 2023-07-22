# -*- coding: utf-8 -*-

import os
import pdfminer
from pdfminer.high_level import extract_text
import json

def extract_text_from_pdf(pdf_path):
    try:
        text = extract_text(pdf_path)
        return text
    except pdfminer.pdfminer.exceptions.PDFSyntaxError:
        #print(f"Error: Unable to extract text from '{pdf_path}'. The PDF may be scanned or corrupted.")
        return None

def text_to_json(pdf_path, sections):
    data = {
        "pdf_path": pdf_path,
        "sections": sections
    }
    return data

def save_as_json(json_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)

def group_paragraphs_into_sections(pdf_text, start_keyword, end_keyword):
    paragraphs = pdf_text.split("\n\n")
    sections = []
    current_section = []

    for paragraph in paragraphs:
        if start_keyword in paragraph:
            print(paragraph)
            if current_section:
                sections.append("\n\n".join(current_section))
               
            current_section = [paragraph]
        elif end_keyword in paragraph:
            current_section.append(paragraph)
            sections.append("\n\n".join(current_section))
            current_section = []
        else:
            current_section.append(paragraph)

    if current_section:
        sections.append("\n\n".join(current_section))

    return sections

def process_pdfs_in_folder(input_folder, output_file, start_keyword, end_keyword):
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith(".pdf")]

    all_pdf_data = []
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        pdf_text = extract_text_from_pdf(pdf_path)
        if pdf_text is not None:
            sections = group_paragraphs_into_sections(pdf_text, start_keyword, end_keyword)
            pdf_data = text_to_json(pdf_path, sections)
            all_pdf_data.append(pdf_data)

    save_as_json(all_pdf_data, output_file)

# Replace 'input_folder' with the path to the folder containing your PDFs
input_folder = 'pdf_files/'
# Replace 'output.json' with the desired output file name
output_file = 'output.json'
# Replace 'start_keyword' and 'end_keyword' with the special keywords that mark the start and end of each section
start_keyword = 'NỘI DUNG VỤ ÁN:'
end_keyword = 'NHẬN ĐỊNH CỦA TÒA ÁN:'

process_pdfs_in_folder(input_folder, output_file, start_keyword, end_keyword)


print(f"Text content from PDFs in '{input_folder}' saved to '{output_file}' as JSON with grouped sections.")
