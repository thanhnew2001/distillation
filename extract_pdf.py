# -*- coding: utf-8 -*-

import os
import pdfplumber
import pandas as pd

def extract_sections_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    # Split the text into paragraphs
    paragraphs = text.split('\n\n')

    # Initialize variables to store section content
    sections = {
        'File': pdf_path,
        'tenbanan': "",
        'thamphan': "",
        'thuky': "",
        'vienkiemsat': "",
        'nguoikhoikien': "",
        'nguoibikien': "",
        'noidungvuan': "",
        'nhandinhtoaan': "",
        'quyetdinh': "",
    }

    # Identify and store paragraphs in the corresponding sections based on keywords
    current_section = None
    for paragraph in paragraphs:
        # Clean the paragraph text by removing leading/trailing whitespaces and newlines
        paragraph = paragraph.strip()

        # Skip empty paragraphs
        if not paragraph:
            continue

        # Identify the section based on the content or keywords
        if "Số:" in paragraph.lower():
            current_section = "tenbanan"
        elif "Thẩm phán" in paragraph.lower():
            current_section = "thamphan"
        elif "Thư ký" in paragraph.lower():
            current_section = "thuky"
        elif "Viện kiểm sát" in paragraph.lower():
            current_section = "vienkiemsat"
        elif "Ngừoi khởi kiện" in paragraph.lower():
            current_section = "nguoikhoikien"
        elif "Ngừoi bị kiện" in paragraph.lower():
            current_section = "nguoibikien"
        elif "Nội dung vụ án" in paragraph.lower():
            current_section = "noidungvuan"
        elif "Nhận định toà án" in paragraph.lower():
            current_section = "nhandinhtoaan"
        elif "Quyết định" in paragraph.lower():
            current_section = "quyetdinh"

        # Store the paragraph in the corresponding section
        if current_section and current_section in sections:
            sections[current_section] += paragraph + "\n"

    # Remove leading/trailing whitespaces and newlines from the section content
    for section_name in sections:
        sections[section_name] = sections[section_name].strip()

    return sections

# Replace 'your_pdf_folder' with the path to the folder containing your PDF files
pdf_folder = 'pdf_files'

# List all PDF files in the specified folder
pdf_files = [os.path.join(pdf_folder, file) for file in os.listdir(pdf_folder) if file.endswith('.pdf')]

data = []
for pdf_file in pdf_files:
    section_data = extract_sections_from_pdf(pdf_file)
    data.append(section_data)

# Create a Pandas DataFrame from the extracted data
df = pd.DataFrame(data)

# Now you have the specified sections extracted from all PDF files
print(df)
df.to_json("data.json", orient='table')
