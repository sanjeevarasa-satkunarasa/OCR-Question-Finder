import os
from bs4 import BeautifulSoup

# Define the subject variable
subject = "1P"  # You can change this to any subject you want

html_content = """
<li>
                    <h3>V2024</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_V24.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>H2023</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_H23.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>V2023</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_V23.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>H2022</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_H22_LK20.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>V2022</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_V22_LK20.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>H2021</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/EVH-2021MAT1019____F01S.pdf" target="_blank" download> Oppgave </a>
                </li>
                <li><a href="/eksamensoppgaver/1P/Eksempelsett_1P_H21.pdf" target="_blank" download> Oppgave (Eksempel)
                    </a>
                </li>
                <li>
                    <h3>V2021</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_V21_LK20.pdf" target="_blank" download> Oppgave </a></li>
                <li><a href="/eksamensoppgaver/1P/1P  V21 LK20 eksempel 2.pdf" target="_blank" download> Oppgave
                        (Eksempel)
                    </a></li>
                <li>
                    <h3>H2020</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_H20.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>V2020</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/Eksamen 1P V2020.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>H2019</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_H19.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>V2019</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/EVV-2019MAT1011____F02S.pdf" target="_blank" download> Oppgave </a>
                </li>
                <li>
                    <h3>H2018</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_H18.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>V2018</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_V18.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>H2017</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_H17.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>V2017</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_V17.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>H2016</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_H16.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>V2016</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_V16.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>H2015</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_H15.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>V2015</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_V15.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>H2014</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_H14.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>V2014</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_V14.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>H2013</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_H13.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>V2013</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_V13.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>H2012</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_H12.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>V2012</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_V12.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>H2011</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_H11.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>V2011</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_V11.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>H2010</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_H10.pdf" target="_blank" download> Oppgave </a></li>
                <li>
                    <h3>V2010</h3>
                </li>
                <li><a href="/eksamensoppgaver/1P/1P_V10.pdf" target="_blank" download> Oppgave </a></li>
"""

base_path = r"G:\My Drive\Personal\Programming\Projects\OCR Question Bank\OCR-Question-Finder"

soup = BeautifulSoup(html_content, 'html.parser')
result = {}

# Parse the HTML content and create the dictionary
for h3 in soup.find_all('h3'):
    if len(h3.text) == 5:
        anchor = h3.find_next('a', href=True)
        if anchor and '/eksamensoppgaver/' in anchor['href']:
            full_path = base_path + anchor['href'].replace('/', '\\')
            full_path = full_path.replace('\\\\', '\\').replace('\\', '/')
            result[h3.text] = full_path

# Rename the files according to the specified format and update the HTML content
for key, path in result.items():
    # Extract the directory and the file extension
    directory, old_filename = os.path.split(path)
    file_extension = os.path.splitext(old_filename)[1]
    
    # Create the new filename
    new_filename = f"Eksamen_{subject}_{key}{file_extension}"
    
    # Create the full path for the new filename
    new_path = os.path.join(directory, new_filename)
    
    # Rename the file, ignoring case sensitivity
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower() == old_filename.lower():
                os.rename(os.path.join(root, file), new_path)
                print(f"Renamed '{os.path.join(root, file)}' to '{new_path}'")
                break
    
    # Update the anchor tag in the HTML content
    for anchor in soup.find_all('a', href=True):
        if anchor['href'].lower().endswith(old_filename.lower()):
            anchor['href'] = anchor['href'].replace(old_filename, new_filename)

# Write the updated HTML content to a text file
updated_html_content = soup.prettify()
with open("updated_html_content.txt", "w", encoding="utf-8") as file:
    file.write(updated_html_content)

print("Updated HTML content has been written to 'updated_html_content.txt'")
