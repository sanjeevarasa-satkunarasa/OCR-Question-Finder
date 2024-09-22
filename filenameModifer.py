import os
from bs4 import BeautifulSoup

def extract_data_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        # Extracting the subject title from h1
        subject = soup.find('h1', class_='subject-title').get_text()

        # Finding all h3 tags (for term/year) and corresponding PDF links
        term_years = [h3.get_text() for h3 in soup.find_all('h3')]
        pdf_links = []
        for a in soup.find_all('a', href=True):
            if a['href'].endswith('.pdf'):
                pdf_links.append(a['href'])

        # Extracting the filepath of each PDF
        pdf_filepaths = []
        for link in pdf_links:
            filepath = link.split('/')[-1]  # Get the filename from the URL
            pdf_filepaths.append(filepath)

        return subject, term_years, pdf_links, pdf_filepaths

def rename_pdfs(directory, html_file):
    # Extract subject, term/year, and PDF links from HTML
    subject, term_years, pdf_links, pdf_filepaths = extract_data_from_html(html_file)

    # Get all PDF files in the directory (assuming the files are in order)
    pdf_files = sorted([f for f in os.listdir(directory) if f.endswith('.pdf')])

    # Mismatch Check
    num_links = len(pdf_links)
    num_pdfs = len(pdf_files)

    if num_links != num_pdfs:
        # Mismatch detected: Provide feedback on the mismatch
        print(f"Mismatch detected:")
        print(f" - Number of PDFs in directory: {num_pdfs}")
        print(f" - Number of PDF links in HTML: {num_links}")

        if num_pdfs > num_links:
            print(f"Extra PDF files found: {num_pdfs - num_links}")
        else:
            print(f"Missing PDF files: {num_links - num_pdfs}")
        return

    # Loop through PDFs and rename them based on subject and term/year
    for i, pdf in enumerate(pdf_files):
        term_year = term_years[i]  # Get the corresponding term/year (e.g., "V2024")
        filepath = pdf_filepaths[i]  # Get the corresponding filepath
        new_name = f"{subject}_{term_year}_{filepath}"  # Construct the new name

        # Construct the full file paths
        old_file = os.path.join(directory, pdf)
        new_file = os.path.join(directory, new_name)

        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {pdf} -> {new_name}")

# Example usage:
directory = 'S1'
html_file = 'html\VG2.html'
rename_pdfs(directory, html_file)