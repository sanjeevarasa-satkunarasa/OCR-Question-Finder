export default function processInput() {
    const textInput = document.getElementById('textInput').value;
    const fileInput = document.getElementById('fileInput').files[0];
    let output;

    if (textInput && fileInput) {
        alert("There are two inputs given. Please provide only one input.");
        return;
    }

    if (textInput) {
        output = textInput;
        document.getElementById('question-output').innerText = output;
        console.log("Text input:", output);
        sendDataToPython(output);
    } else if (fileInput) {
        const reader = new FileReader();
        reader.onload = function(event) {
            output = event.target.result;
            document.getElementById('question-output').innerText = output;
            console.log("File content:", output);
            sendDataToPython(output);
        };
        reader.readAsText(fileInput, 'UTF-8'); // Ensure the file is read as UTF-8
    } else {
        output = "No input provided";
        document.getElementById('question-output').innerText = output;
    }
}

function sendDataToPython(data) {
    const fs = require('fs');
    const { exec } = require('child_process');

    // Write JSON data to a file
    fs.writeFileSync('data.json', JSON.stringify({ input: data }));

    // Execute the Python script
    exec('python data_receiver.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`Stderr: ${stderr}`);
            return;
        }
        console.log(`Output: ${stdout}`);
    });
}
