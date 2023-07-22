import os
import docx2txt
import chardet

def convert_docx_to_txt(docx_file, output_folder):
    try:
        txt_content = docx2txt.process(docx_file)
        txt_file = os.path.splitext(os.path.basename(docx_file))[0] + ".txt"
        txt_path = os.path.join(output_folder, txt_file)

        with open(txt_path, "w", encoding="utf-8") as txt_output:
            txt_output.write(txt_content)
    except Exception as e:
        print(f"Error: Unable to convert {docx_file} to txt - {str(e)}")

def merge_txt_files(input_folder, output_file):
    with open(output_file, "w", encoding="utf-8") as merged_output:
        for txt_file in os.listdir(input_folder):
            if txt_file.endswith(".txt"):
                txt_path = os.path.join(input_folder, txt_file)
                with open(txt_path, "rb") as txt_input:
                    raw_data = txt_input.read()
                    detected_encoding = chardet.detect(raw_data)['encoding']
                    try:
                        txt_content = raw_data.decode(detected_encoding)
                        merged_output.write(txt_content)
                    except UnicodeDecodeError:
                        print(f"Error: Unable to decode file '{txt_file}' with detected encoding '{detected_encoding}'.")

# Replace 'input_folder' with the path to the folder containing your .docx files
input_folder = 'translate39/'
# Replace 'output_folder' with the path where you want to store the .txt files
output_folder = 'translate39/merge'
# Replace 'merged.txt' with the desired output file name for the merged .txt file
output_file = 'merged39.txt'

# Convert .docx files to .txt files
for docx_file in os.listdir(input_folder):
    if docx_file.endswith(".docx"):
        docx_path = os.path.join(input_folder, docx_file)
        convert_docx_to_txt(docx_path, output_folder)

# Merge .txt files into a single .txt file
merge_txt_files(output_folder, output_file)

print(f"Converted .docx files in '{input_folder}' to .txt files in '{output_folder}'.")
print(f"Merged .txt files into '{output_file}'.")
