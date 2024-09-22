import subprocess
import os
import pymongo
# from mongo_module import insert_mangodb

# Test command to ensure ocrmypdf works
subprocess.run("wsl ocrmypdf --sidecar 1T_H12.txt --force-ocr 1T_H12.pdf 1T_H12_output.pdf")

# Directory containing the PDF files
directory = r'G:\My Drive\Personal\Programming\Projects\OCR Question Bank\OCR-Question-Finder\1T Files'

# Function to convert Windows path to WSL path
def convert_to_wsl_path(win_path):
    return subprocess.run(['wsl', 'wslpath', '-a', win_path], capture_output=True, text=True).stdout.strip()

# Function to process PDF files
def process_pdfs(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.pdf'):
                # Full path to the PDF file
                pdf_path = os.path.join(root, filename)
                wsl_pdf_path = convert_to_wsl_path(pdf_path)
                
                # Output file path
                output_file = os.path.join(root, f'{os.path.splitext(filename)[0]}_output.pdf')
                wsl_output_file = convert_to_wsl_path(output_file)
                
                sidecar_file = os.path.join(root, f'{os.path.splitext(filename)[0]}.txt')
                wsl_sidecar_file = convert_to_wsl_path(sidecar_file)
                
                try:
                    # Debug print statements
                    print(f'PDF path: {pdf_path} (WSL: {wsl_pdf_path})')
                    print(f'Output file path: {output_file} (WSL: {wsl_output_file})')
                    print(f'Sidecar file path: {sidecar_file} (WSL: {wsl_sidecar_file})')
                    
                    # Run ocrmypdf command in WSL
                    result = subprocess.run(['wsl', 'ocrmypdf', '--sidecar', wsl_sidecar_file, '--force-ocr', wsl_pdf_path, wsl_output_file], check=True, capture_output=True, text=True)
                    print(f'ocrmypdf command result: {result}')
                    print(f'Stdout: {result.stdout}')
                    print(f'Stderr: {result.stderr}')
                    
                    # Check if sidecar file was created
                    if os.path.exists(sidecar_file):
                        print(f'Sidecar file created: {sidecar_file}')
                        # Read the output file
                        with open(sidecar_file, 'r') as file:
                            content = file.read()
                        
                        # Insert into MongoDB
                        # insert_mangodb(output_file, content)
                    else:
                        print(f'Sidecar file not found: {sidecar_file}')
                except subprocess.CalledProcessError as e:
                    print(f'Error processing {pdf_path}: {e}')
                    print(f'Stdout: {e.stdout}')
                    print(f'Stderr: {e.stderr}')
                except Exception as e:
                    print(f'Unexpected error: {e}')

# Start processing
process_pdfs(directory)

print("Processing complete.")
