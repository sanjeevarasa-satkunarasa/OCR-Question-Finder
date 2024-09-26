import os
import subprocess
from PIL import Image

# Path to the file
file_path = r'G:\My Drive\Personal\Programming\Projects\OCR Question Bank\OCR-Question-Finder\eksamensoppgaver\your_file.jpg'

# Function to convert Windows path to WSL path
def convert_to_wsl_path(win_path):
    return subprocess.run(['wsl', 'wslpath', '-a', win_path], capture_output=True, text=True).stdout.strip()

# Function to convert image to PDF
def convert_image_to_pdf(image_path):
    image = Image.open(image_path)
    pdf_path = os.path.splitext(image_path)[0] + '.pdf'
    image.save(pdf_path, 'PDF', resolution=100.0)
    return pdf_path

# Function to process a single file
def process_file(file_path):
    # Check if the file is an image
    if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')):
        file_path = convert_image_to_pdf(file_path)
    
    wsl_file_path = convert_to_wsl_path(file_path)
    
    # Output file path
    output_file = os.path.splitext(file_path)[0] + '_output.pdf'
    wsl_output_file = convert_to_wsl_path(output_file)
    
    sidecar_file = os.path.splitext(file_path)[0] + '.txt'
    wsl_sidecar_file = convert_to_wsl_path(sidecar_file)
    
    try:
        # Debug print statements
        print(f'File path: {file_path} (WSL: {wsl_file_path})')
        print(f'Output file path: {output_file} (WSL: {wsl_output_file})')
        print(f'Sidecar file path: {sidecar_file} (WSL: {wsl_sidecar_file})')
        
        # Run ocrmypdf command in WSL
        result = subprocess.run(['wsl', 'ocrmypdf', '--sidecar', wsl_sidecar_file, '--force-ocr', wsl_file_path, wsl_output_file], check=True, capture_output=True, text=True)
        print(f'ocrmypdf command result: {result}')
        print(f'Stdout: {result.stdout}')
        print(f'Stderr: {result.stderr}')
        
        # Check if sidecar file was created
        if os.path.exists(sidecar_file):
            print(f'Sidecar file created: {sidecar_file}')
            # Read the output file
            with open(sidecar_file, 'r') as file:
                content = file.read()
            
            # Return the content
            return content
        else:
            print(f'Sidecar file not found: {sidecar_file}')
            return None
    except subprocess.CalledProcessError as e:
        print(f'Error processing {file_path}: {e}')
        print(f'Stdout: {e.stdout}')
        print(f'Stderr: {e.stderr}')
        return None
    except Exception as e:
        print(f'Unexpected error: {e}')
        return None

# Process the file
ocr_output = process_file(file_path)

# Print the OCR output
if ocr_output:
    print(f'OCR Output:\n{ocr_output}')

print("Processing complete.")
