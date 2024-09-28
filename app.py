from flask import Flask, request, redirect, url_for, render_template_string, flash
import os
import subprocess
from PIL import Image
import pymongo
from difflib import SequenceMatcher

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flashing messages

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Variable to store the output
output = ""

@app.route('/')
def index():
    global output
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="nb">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="keywords" content="science, study tools, study tool, realfag, realfag.net">
        <meta name="description" content="Nettstedet som gjør realfag enklere og har et oppgave gjennkjennelsesprogram">
        <meta name="author" content="Nover Studio">
        <link rel="stylesheet" href="css/styles.css" id="theme-style">
        <title>Realfag.net</title>
        <link rel="icon" type="image/x-icon" href="/media/favicon_light.ico" id="favicon">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
        <script src="/script.js" defer></script>
    </head>
    <body>
        <nav>
            <h1><a href="../index.html">Realfag.net</a></h1>
            <a href="/html/info.html">Info</a>
            <a onclick="toggleMode(false)" id="dark_mode">Toggle Dark Mode</a>
        </nav>
        <div class="ambitions">
            <h1 class="ambitions-text">Nettstedet som gjør læring enkelt</h1>
        </div>
        <div class="ocr-program">
            <h3 class="ocr-program-heading">Program som finner fram til oppgaven din</h3>
            <form class="question-form" action="/upload" method="post" enctype="multipart/form-data">
                <textarea id="textInput" name="question-text" rows="6" cols="75" placeholder="Skriv inn oppgaven" class="question-text"></textarea>
                <br>
                <label for="file-upload" class="custom-file-upload"> Klikk for å laste opp filer</label>
                <input id="fileInput" name="file-upload" type="file" />
                <input type="submit" class="question-submit" value="Submit">
            </form>
            <div class="question-output-container">
                <h4>Output:</h4>
                <h4 id="question-output">{{ output }}</h4>
            </div>
            {% with messages = get_flashed_messages() %}
                {% if messages %}
                    <ul class="flashes">
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                    </ul>
                {% endif %}
            {% endwith %}
        </div>
        <div class="support">
            <h1>Støtt oss!</h1>
            <h3>Støtt oss ved å gi dine oppgaver/prøver/løsningsforslag!</h3>
            <div class="form">
                <form netlify method="POST">
                    <label class="form-title">Skjema for innsending:</label>
                    <br>
                    <label for="year">Årstall (åååå)</label>
                    <input type="number" name="year" min="1950" max="2025">
                    <br>
                    <label for="school">Skolenavn:</label>
                    <input list="school">
                    <datalist id="school">
                        <option value="Nydalen VGS">
                        <option value="Elvebakken VGS">
                        <option value="Edvard Munch VGS">
                        <option value="F21 VGS">
                    </datalist>
                    <br>
                    <label for="description">Beskrivelse</label>
                    <textarea name="description" rows="4" cols="50"></textarea>
                    <br>
                    <input type="submit" value="Send inn">
                </form>
            </div>
        </div>
    </body>
    </html>
    ''', output=output)

@app.route('/upload', methods=['POST'])
def upload_file():
    global output
    text = request.form.get('question-text')
    file = request.files.get('file-upload')

    if text and file:
        flash("Det kan ikke være to inputter")
        return redirect(url_for('index'))
    elif file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        ocr_output = process_file(file_path)
        output = format_output(get_most_similar_document_key(ocr_output, "admin", "results"))
    elif text:
        output = format_output(get_most_similar_document_key(text, "admin", "results"))
    else:
        output = "No input provided"

    return redirect(url_for('index'))

def convert_to_wsl_path(win_path):
    return subprocess.run(['wsl', 'wslpath', '-a', win_path], capture_output=True, text=True).stdout.strip()

def convert_image_to_pdf(image_path):
    image = Image.open(image_path)
    pdf_path = os.path.splitext(image_path)[0] + '.pdf'
    image.save(pdf_path, 'PDF', resolution=100.0)
    return pdf_path

def process_file(file_path):
    if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')):
        file_path = convert_image_to_pdf(file_path)
    
    wsl_file_path = convert_to_wsl_path(file_path)
    output_file = os.path.splitext(file_path)[0] + '_output.pdf'
    wsl_output_file = convert_to_wsl_path(output_file)
    sidecar_file = os.path.splitext(file_path)[0] + '.txt'
    wsl_sidecar_file = convert_to_wsl_path(sidecar_file)
    
    try:
        result = subprocess.run(['wsl', 'ocrmypdf', '--sidecar', wsl_sidecar_file, '--force-ocr', wsl_file_path, wsl_output_file], check=True, capture_output=True, text=True)
        
        if os.path.exists(sidecar_file):
            with open(sidecar_file, 'r') as file:
                content = file.read()
            return content
        else:
            return 'Sidecar file not found'
    except subprocess.CalledProcessError as e:
        return f'Error processing {file_path}: {e}'
    except Exception as e:
        return f'Unexpected error: {e}'

def get_most_similar_document_key(input_string, db_name, collection_name):
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]

    most_similar_key = None
    highest_similarity = 0

    # Iterate through all documents in the collection
    for document in collection.find():
        value = document.get("value", "")
        if isinstance(value, str):
            similarity = SequenceMatcher(None, input_string, value).ratio()
            if similarity > highest_similarity:
                highest_similarity = similarity
                most_similar_key = document.get("key")

    return most_similar_key

def format_output(output):
    if output:
        output = output.replace(".pdf", "").replace("_", " ")
    return output

if __name__ == '__main__':
    app.run(debug=True)
