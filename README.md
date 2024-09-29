# OCR-Question-Finder

This program was created for [realfag.net](https://realfag.net/) in order to help Norwegian student find the source of their question, so that they can use the appropriate answer sheet.

## Background

I've realised that a lot of past papers have similar question. For someone who's gone through a lot of papers it's a lot easier to recognise if a question is a past question, but for someone less experience, it isn't as easy. That's why a tool like the one I've now created can be used to find solutions quicker and easier for both experienced and inexperienced.

## General Overview

- Setup

- Functionality & Limitations

- How it works

## Setup & Requirements

### Requirements

**Currently only supports Linux and Windows**

You will need to install MongoDB and will also need files to put into the program

### Setup
1. Install Python packages
`
pip install -r requirements.txt
`

2. Install system packages on WSL
`
sudo apt install ocrmypdf
sudo apt-get install tesseract-ocr-nor
`
 
## Functionality & Limitations

You can put about any file that has text in it through the program. However, it should be noted that the OCR program is configured to work with languages with Latin alphabets but this is something you can modify in **main.py**.


## How it works
### Project Overview

This project processes exam questions using OCR and stores them in a MongoDB database. The workflow is as follows:

1.  **Input Files**: The files you want to compare are processed by  `main.py`  to perform OCR and store the results in the MongoDB database.
    
2.  **User Input**: The program constantly checks for new inputs from the user via the  `index.html`  page. This can be either a file or text input. The script responsible for this is  `app.py`.
    
3.  **Processing Input**:
    
    -   **File Input**: If the input is a file, it is processed by  `input_ocr.py`  for OCR and then passed to  `ranking_system.py`.
    -   **Text Input**: If the input is text, it is directly processed by  `ranking_system.py`.
4.  **Output**: The output is the key value from the database, which is displayed to the user on the website. This is handled by  `app.py`  by inputting the key value as a string into the program.