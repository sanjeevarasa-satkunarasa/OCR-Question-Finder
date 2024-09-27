import os
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def check_paths(folder_path, html_file_path):
    if not os.path.exists(folder_path):
        logging.error(f"The folder path '{folder_path}' does not exist.")
        exit(1)
    if not os.path.exists(html_file_path):
        logging.error(f"The HTML file path '{html_file_path}' does not exist.")
        exit(1)

def parse_html(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    subject_title = soup.find('h1', class_='subject-title').text.strip()
    file_info = []
    for h3 in soup.find_all('h3'):
        year = h3.text.strip()
        for a in h3.find_next_siblings('a', href=True):
            file_name = os.path.basename(a['href']).strip().replace(' ', '_')
            new_name = f"Eksamen_{subject_title}_{year}".strip().replace(' ', '_')
            file_info.append((file_name, new_name))
    return file_info

def rename_files(folder_path, file_info):
    for old_name, new_name in file_info:
        old_full_path = os.path.join(folder_path, old_name).replace(' ', '_')
        new_full_path = os.path.join(folder_path, new_name + os.path.splitext(old_name)[1]).replace(' ', '_')
        logging.debug(f"Renaming '{old_full_path}' to '{new_full_path}'")
        if os.path.exists(old_full_path):
            os.rename(old_full_path, new_full_path)
        else:
            logging.error(f"The file '{old_full_path}' does not exist.")

def main():
    folder_path = r'G:\MyDrive\Personal\Programming\Projects\OCR Question Bank\OCR-Question-Finder\eksamensoppgaver\R1'
    html_file_path = r'G:\MyDrive\Personal\Programming\Projects\OCR Question Bank\OCR-Question-Finder\test.html'
    
    logging.debug(f"Folder path: {folder_path}")
    logging.debug(f"HTML file path: {html_file_path}")
    
    check_paths(folder_path, html_file_path)
    file_info = parse_html(html_file_path)
    
    logging.debug("Extracted file information:")
    for old_name, new_name in file_info:
        logging.debug(f"Old name: {old_name}, New name: {new_name}")
    
    rename_files(folder_path, file_info)
    logging.info("Files have been renamed successfully!")

if __name__ == "__main__":
    main()
