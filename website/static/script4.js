const dragArea = document.getElementById('drag-area');
const dragText = document.getElementById('dragText');
const dragLabel = document.getElementById('labelDrag');
let file;

dragArea.addEventListener('dragover', (event) => {
    dragText.innerHTML = "Drop Here to upload.";
    dragLabel.classList.add('active');
    console.log("In drag area...");
});

dragArea.addEventListener('dragleave', () => {
    dragText.innerHTML = "Click to upload or drag and drop.";
    dragLabel.classList.remove('active');
});

dragArea.addEventListener('drop', (event) => {
    event.preventDefault();

    file = event.dataTransfer.files[0];
    let filetype = file.type;
    console.log(filetype); 

});