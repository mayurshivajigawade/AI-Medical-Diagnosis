// ==========================================
// AI Medical Diagnosis Assistant
// Image Preview & Validation
// ==========================================

const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5 MB

function previewImage(event) {

    const file = event.target.files[0];

    const preview = document.getElementById("preview");

    // No file selected
    if (!file) {

        preview.style.display = "none";

        return;

    }

    // Check file type
    const allowedTypes = [

        "image/jpeg",

        "image/jpg",

        "image/png"

    ];

    if (!allowedTypes.includes(file.type)) {

        alert("Please select a JPG, JPEG or PNG image.");

        event.target.value = "";

        preview.style.display = "none";

        return;

    }

    // Check file size
    if (file.size > MAX_FILE_SIZE) {

        alert("Image size must be less than 5 MB.");

        event.target.value = "";

        preview.style.display = "none";

        return;

    }

    // Show preview
    const reader = new FileReader();

    reader.onload = function(e) {

        preview.src = e.target.result;

        preview.style.display = "block";

        preview.style.opacity = "0";

        preview.style.transform = "scale(0.9)";

        setTimeout(() => {

            preview.style.transition = "0.4s";

            preview.style.opacity = "1";

            preview.style.transform = "scale(1)";

        }, 100);

    };

    reader.readAsDataURL(file);

}

// ==========================================
// Drag & Drop Upload
// ==========================================

const uploadCard = document.querySelector(".upload-card");

const fileInput = document.getElementById("image");

if (uploadCard && fileInput) {

    uploadCard.addEventListener("dragover", function(e) {

        e.preventDefault();

        uploadCard.style.borderColor = "#1565C0";

        uploadCard.style.background = "#E3F2FD";

    });

    uploadCard.addEventListener("dragleave", function() {

        uploadCard.style.borderColor = "#90CAF9";

        uploadCard.style.background = "#F8FBFF";

    });

    uploadCard.addEventListener("drop", function(e) {

        e.preventDefault();

        uploadCard.style.borderColor = "#90CAF9";

        uploadCard.style.background = "#F8FBFF";

        const files = e.dataTransfer.files;

        if (files.length > 0) {

            fileInput.files = files;

            previewImage({ target: fileInput });

        }

    });

}