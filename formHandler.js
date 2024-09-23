function processInput() {
    const textInput = document.getElementById('textInput').value;
    const fileInput = document.getElementById('fileInput').files[0];
    let output;

    if (textInput) {
        output = textInput;
        saveToFile(output, 'textInput.txt');
    } else if (fileInput) {
        const reader = new FileReader();
        reader.onload = function(event) {
            output = event.target.result;
            saveToFile(output, fileInput.name);
        };
        reader.onerror = function(event) {
            console.error("File could not be read! Code " + event.target.error.code);
        };
        reader.readAsText(fileInput, 'UTF-8'); // Ensure the file is read as UTF-8
    } else {
        output = "No input provided";
        document.getElementById('question-output').innerText = output;
    }
}

function saveToFile(content, filename) {
    const blob = new Blob([content], { type: 'text/plain;charset=utf-8' }); // Ensure the file is saved as UTF-8
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}
