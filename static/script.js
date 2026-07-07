// =========================================
// DOM ELEMENTS
// =========================================

const fileInput =
document.getElementById("file-upload");

const previewImage =
document.getElementById("preview-image");

const previewContainer =
document.getElementById("preview-container");

const uploadStatus =
document.getElementById("upload-status");

const fileName =
document.getElementById("file-name");

const predictButton =
document.getElementById("predict-btn");

const progressFill =
document.querySelector(".progress-fill");

const form =
document.querySelector("form");

const uploadBox =
document.getElementById("upload-box");

const logo =
document.querySelector(".logo");



// =========================================
// SHOW IMAGE PREVIEW
// =========================================

function showPreview(file){

    // Check file
    if(!file){

        return;

    }


    // =====================================
    // FILE NAME
    // =====================================

    fileName.textContent =
    file.name;


    // =====================================
    // SUCCESS STATUS
    // =====================================

    uploadStatus.classList.add(
        "success"
    );


    // =====================================
    // FILE EXTENSION
    // =====================================

    const extension =

        file.name
            .split(".")
            .pop()
            .toLowerCase();


    // =====================================
    // IMAGE FILE
    // =====================================

    if(

        extension === "jpg" ||

        extension === "jpeg" ||

        extension === "png"

    ){

        // Create image URL
        const imageURL =
        URL.createObjectURL(file);


        // Show image
        previewImage.src =
        imageURL;


        // Show preview container
        previewContainer.style.display =
        "flex";


        // Fade animation
        previewContainer.classList.add(
            "active-preview"
        );


        // Display image
        previewImage.style.display =
        "block";


        // Upload box effect
        uploadBox.classList.add(
            "uploaded"
        );

    }


    // =====================================
    // NON IMAGE FILE
    // =====================================

    else{

        previewContainer.style.display =
        "none";

    }

}



// =========================================
// FILE CHANGE EVENT
// =========================================

if(fileInput){

    fileInput.addEventListener(

        "change",

        function(event){

            const file =
            event.target.files[0];

            showPreview(file);

        }

    );

}



// =========================================
// PREVENT DEFAULT DRAG
// =========================================

[
    "dragenter",
    "dragover",
    "dragleave",
    "drop"
].forEach(eventName => {

    uploadBox.addEventListener(

        eventName,

        preventDefaults,

        false

    );

});



function preventDefaults(e){

    e.preventDefault();

    e.stopPropagation();

}



// =========================================
// DRAG ACTIVE EFFECT
// =========================================

[
    "dragenter",
    "dragover"
].forEach(eventName => {

    uploadBox.addEventListener(

        eventName,

        () => {

            uploadBox.classList.add(
                "drag-active"
            );

        }

    );

});



// =========================================
// REMOVE DRAG EFFECT
// =========================================

[
    "dragleave",
    "drop"
].forEach(eventName => {

    uploadBox.addEventListener(

        eventName,

        () => {

            uploadBox.classList.remove(
                "drag-active"
            );

        }

    );

});



// =========================================
// HANDLE FILE DROP
// =========================================

uploadBox.addEventListener(

    "drop",

    function(e){

        // Get dropped files
        const files =
        e.dataTransfer.files;


        // Assign files to input
        fileInput.files =
        files;


        // Show preview
        showPreview(files[0]);

    }

);



// =========================================
// LOADING BUTTON EFFECT
// =========================================

if(form){

    form.addEventListener(

        "submit",

        function(){

            // Disable button
            predictButton.disabled =
            true;


            // Add loading class
            predictButton.classList.add(
                "loading"
            );


            // Change button text
            predictButton.innerHTML =

            `
            <i class="fas fa-spinner fa-spin"></i>
            AI sedang menganalisis...
            `;

        }

    );

}



// =========================================
// PROGRESS BAR ANIMATION
// =========================================

if(progressFill){

    // Get confidence value
    const confidence =
    progressFill.dataset.width;


    // Delay animation
    setTimeout(() => {

        progressFill.style.width =
        confidence + "%";

    }, 400);

}



// =========================================
// FLOATING LOGO EFFECT
// =========================================

if(logo){

    let floating = 0;

    setInterval(() => {

        floating += 0.05;

        logo.style.transform =

        `
        translateY(
            ${Math.sin(floating) * 6}px
        )
        `;

    }, 16);

}



// =========================================
// SMOOTH APPEAR ANIMATION
// =========================================

const cards = document.querySelectorAll(

    ".feature-card, .info-card, .ai-panel"

);


cards.forEach((card, index) => {

    card.style.opacity = "0";

    card.style.transform =
    "translateY(20px)";


    setTimeout(() => {

        card.style.transition =
        "all 0.7s ease";

        card.style.opacity = "1";

        card.style.transform =
        "translateY(0px)";

    }, 150 * index);

});



// =========================================
// GLOW EFFECT ON MOUSE MOVE
// =========================================

document.addEventListener(

    "mousemove",

    function(e){

        const x =
        e.clientX / window.innerWidth;

        const y =
        e.clientY / window.innerHeight;


        document.body.style.background =

        `
        radial-gradient(
            circle at
            ${x * 100}% ${y * 100}%,
            rgba(0,255,170,0.10),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #001f1a,
            #004d3d,
            #008066
        )
        `;

    }

);



// =========================================
// UPLOAD BOX HOVER SOUNDLESS FEEL
// =========================================

uploadBox.addEventListener(

    "mouseenter",

    () => {

        uploadBox.style.transform =
        "translateY(-4px)";

    }

);



uploadBox.addEventListener(

    "mouseleave",

    () => {

        uploadBox.style.transform =
        "translateY(0px)";

    }

);



// =========================================
// AUTO SCROLL TO RESULT
// =========================================

window.addEventListener(

    "load",

    () => {

        const resultSection =
        document.querySelector(
            ".result-section"
        );


        if(resultSection){

            setTimeout(() => {

                resultSection.scrollIntoView({

                    behavior: "smooth",

                    block: "center"

                });

            }, 500);

        }

    }

);



// =========================================
// PREMIUM BUTTON GLOW
// =========================================

if(predictButton){

    setInterval(() => {

        predictButton.classList.toggle(
            "pulse"
        );

    }, 2000);

}