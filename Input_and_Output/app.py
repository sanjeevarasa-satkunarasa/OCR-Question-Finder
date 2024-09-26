from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

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
    return '''
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
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    global output
    text = request.form.get('question-text')
    file = request.files.get('file-upload')
    
    if text or file:
        response = ''
        if text:
            text_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'submitted_text.txt')
            with open(text_file_path, 'w') as text_file:
                text_file.write(text)
            response += f'Text saved to: {text_file_path}<br>'
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            response += f'File saved to: {file_path}'
        output = response
        return redirect(url_for('index'))
    output = 'No text or file uploaded'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
