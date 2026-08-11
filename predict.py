import tensorflow as tf
import numpy as np

# Load model
model = tf.keras.models.load_model("pneumonia_cnn.keras")

# Image path
image_path = "test_image.jpg"

# Load image
img = tf.keras.utils.load_img(
    image_path,
    target_size=(224,224)
)

# Convert image to array
img_array = tf.keras.utils.img_to_array(img)

# If your model already contains layers.Rescaling(1./255),
# DO NOT normalize again.
# Otherwise uncomment the next line.
# img_array = img_array / 255.0

# Add batch dimension
img_array = np.expand_dims(img_array, axis=0)

# Predict
prediction = model.predict(img_array)

# Class labels
class_names = ["NORMAL","PNEUMONIA"]

predicted_class = np.argmax(prediction)

confidence = prediction[0][predicted_class] * 100

print("\nPrediction :", class_names[predicted_class])

print(f"Confidence : {confidence:.2f}%")