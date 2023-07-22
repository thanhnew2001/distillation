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
        print(f"Error: '{keyword1}' not found in the PDF.")
        return None

    start_position += len(keyword1)
    end_position = pdf_text.find(keyword2, start_position)
    if end_position == -1:
        print(f"Error: '{keyword2}' not found in the PDF.")
        return None

    return pdf_text[start_position:end_position]

# Replace 'your_file.pdf' with the actual path to your PDF file
pdf_path = 'pdf_files/BAN_AN_TU__NGOC_3_ma_hoa_xong.pdf'

# Step 1: Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Step 2: Define the keywords
# keyword1 = 'start_keyword'
# keyword2 = 'end_keyword'

keyword1 = 'NỘI DUNG VỤ ÁN:'
keyword2 = 'NHẬN ĐỊNH CỦA TÒA ÁN:'

# Step 3: Get the text between the two keywords
selected_text = get_text_between_keywords(pdf_text, keyword1, keyword2)
print(selected_text)
