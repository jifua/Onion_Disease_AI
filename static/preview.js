// ==========================================
// GET HTML ELEMENTS
// ==========================================

const uploadBox = document.getElementById("uploadBox");

const fileInput = document.getElementById("fileInput");

const previewContainer = document.getElementById("previewContainer");

const previewImage = document.getElementById("previewImage");

const previewName = document.getElementById("previewName");


// ==========================================
// OPEN FILE EXPLORER
// ==========================================

uploadBox.addEventListener("click", () => {

    fileInput.click();

});


// ==========================================
// HANDLE FILE SELECTION
// ==========================================

fileInput.addEventListener("change", (event) => {

    const file = event.target.files[0];

    if (file) {

        showPreview(file);

    }

});


// ==========================================
// DRAG OVER EFFECT
// ==========================================

uploadBox.addEventListener("dragover", (event) => {

    event.preventDefault();

    uploadBox.classList.add("drag-active");

});


// ==========================================
// DRAG LEAVE EFFECT
// ==========================================

uploadBox.addEventListener("dragleave", () => {

    uploadBox.classList.remove("drag-active");

});


// ==========================================
// DROP IMAGE
// ==========================================

uploadBox.addEventListener("drop", (event) => {

    event.preventDefault();

    uploadBox.classList.remove("drag-active");

    const file = event.dataTransfer.files[0];

    if (file) {

        fileInput.files = event.dataTransfer.files;

        showPreview(file);

    }

});


// ==========================================
// SHOW IMAGE PREVIEW
// ==========================================

function showPreview(file) {

    // Create file reader
    const reader = new FileReader();


    // Read image
    reader.onload = function (e) {

        // Set image source
        previewImage.src = e.target.result;

        // Set image filename
        previewName.textContent = file.name;

        // Show preview container
        previewContainer.style.display = "block";

    };


    // Read file as URL
    reader.readAsDataURL(file);

}