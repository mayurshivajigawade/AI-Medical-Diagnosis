import tensorflow as tf
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

IMAGE_SIZE = (224,224)
BATCH_SIZE = 32

test_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset/chest_xray/test",
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

model = tf.keras.models.load_model("pneumonia_cnn.keras")

predictions = model.predict(test_dataset)

predicted_labels = np.argmax(predictions, axis=1)

true_labels = np.concatenate([labels for images, labels in test_dataset])

print(confusion_matrix(true_labels, predicted_labels))

print(classification_report(
    true_labels,
    predicted_labels,
    target_names=test_dataset.class_names
))