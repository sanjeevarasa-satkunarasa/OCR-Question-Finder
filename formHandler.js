export default function processInput() {
    const textInput = document.getElementById('textInput').value;

    if (textInput) {
        sendDataToPython(textInput);
    } else {
        console.log("No input provided");
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
