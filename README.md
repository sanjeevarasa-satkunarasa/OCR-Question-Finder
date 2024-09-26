# OCR-Question-Finder
This program was created for [realfag.net](https://realfag.net/) in order to help Norwegian student find the source of their question, so that they can use the appropriate answer sheet.
## Background
I've realised that a lot of past papers have similar question. For someone who's gone through a lot of papers it's a lot easier to recognise if a question is a past question, but for someone less experience, it isn't as easy.  That's why a tool like the one I've now created can be used to find solutions quicker and easier for both experienced and inexperienced. 
## General Overview
 - Setup
 - Functionality & Limitations
 - How it works

## Setup & Requirements
### Requirements
**Currently only supports Linux and Windows**
You will need to have these libraries installed on you computer

    pip install pymongo 
    pip install ...

You will also need to install MongoDB and will also need files to put into the program

### Setup


## Functionality & Limitations
You can put about any file that has text in it through the program. However, it should be noted that the OCR program is configured to work with languages with Latin alphabets but this is something you can modify in **main.py**. 

## How it works
### Background
The files you want the input compared to goes through **main.py** in order to go through OCR and put into the database.
### Roadmap
1. The program constantly checks for new inputs from the user, either as a file or text
2. The input (if a file) goes through the OCR program otherwise (if a text) goes directly into **ranking_system.py**.
3. The output is the key value from the database and that is outputted to the user in the website

