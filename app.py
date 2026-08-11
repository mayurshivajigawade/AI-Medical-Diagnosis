from flask import Flask, render_template, request, redirect, url_for, flash
import tensorflow as tf
import numpy as np
import os
from werkzeug.utils import secure_filename
from database import init_db, save_prediction, get_history

# ==========================================
# Flask Configuration
# ==========================================

app = Flask(__name__)

app.secret_key = "medical_ai_secret_key"

UPLOAD_FOLDER = "static/uploads"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==========================================
# Initialize Database
# ==========================================

init_db()

# ==========================================
# Load AI Model
# ==========================================

MODEL_PATH = "models/pneumonia_cnn.keras"

model = tf.keras.models.load_model(MODEL_PATH)

CLASS_NAMES = [
    "NORMAL",
    "PNEUMONIA"
]

# ==========================================
# Helper Function
# ==========================================

def allowed_file(filename):

    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# Prediction
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:

        flash("No file selected.")

        return redirect("/")

    file = request.files["image"]

    if file.filename == "":

        flash("Please choose an image.")

        return redirect("/")

    if not allowed_file(file.filename):

        flash("Only JPG, JPEG and PNG images are allowed.")

        return redirect("/")

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    try:

        image = tf.keras.utils.load_img(
            filepath,
            target_size=(224, 224)
        )

        image_array = tf.keras.utils.img_to_array(image)

        # Do NOT divide by 255 here because
        # the model already contains Rescaling(1./255)

        image_array = np.expand_dims(
            image_array,
            axis=0
        )

        prediction = model.predict(image_array)

        predicted_index = np.argmax(prediction)

        predicted_class = CLASS_NAMES[predicted_index]

        confidence = float(
            prediction[0][predicted_index] * 100
        )

        # Save into database
        save_prediction(
            filename,
            predicted_class,
            confidence
        )

        return render_template(
            "result.html",
            prediction=predicted_class,
            confidence=f"{confidence:.2f}",
            image=filename
        )

    except Exception as e:

        flash(str(e))

        return redirect("/")


# ==========================================
# Prediction History
# ==========================================

@app.route("/history")
def history():

    records = get_history()

    return render_template(
        "history.html",
        records=records
    )


# ==========================================
# About Page
# ==========================================

@app.route("/about")
def about():

    return render_template("about.html")


# ==========================================
# Contact Page
# ==========================================

@app.route("/contact")
def contact():

    return render_template("contact.html")


# ==========================================
# Error Pages
# ==========================================

@app.errorhandler(404)
def page_not_found(error):

    return "404 - Page Not Found", 404


@app.errorhandler(500)
def internal_error(error):

    return "500 - Internal Server Error", 500


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )