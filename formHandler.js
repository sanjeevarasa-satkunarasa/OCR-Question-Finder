function processInput() {
    const textInput = document.getElementById('textInput').value;
    const fileInput = document.getElementById('fileInput').files[0];
    let output;

    if (textInput) {
        output = textInput;
    } else if (fileInput) {
        const reader = new FileReader();
        reader.onload = function(event) {
            output = event.target.result;
            document.getElementById('question-output').innerText = output;
            console.log("File content:", output);
        };
        reader.readAsText(fileInput);
    } else {
        output = "No input provided";
        document.getElementById('question-output').innerText = output;
    }

    if (textInput) {
        document.getElementById('question-output').innerText = output;
        console.log("Text input:", output);
    }
}