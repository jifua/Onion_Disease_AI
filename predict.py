# ==========================================
# IMPORT LIBRARIES
# ==========================================

import onnxruntime as ort
import numpy as np
import cv2
import os


# ==========================================
# MODEL CONFIGURATION
# ==========================================

MODEL_PATH = "model/onion_disease_model2.onnx"

IMAGE_PATH = "test.jpg"


# ==========================================
# CLASS LABELS
# ==========================================

CLASS_NAMES = [

    "Alternaria_D",

    "Caterpillar-P",

    "Fusarium-D",

    "Healthy leaves",

    "Iris yellow virus_augment",

    "Purple blotch",

    "Virosis-D",

    "Stemphylium Leaf Blight"

]


# ==========================================
# LOAD ONNX MODEL
# ==========================================

print("\nLoading ONNX model...")

session = ort.InferenceSession(
    MODEL_PATH
)

print("Model loaded successfully!")


# ==========================================
# CHECK IMAGE FILE
# ==========================================

if not os.path.exists(IMAGE_PATH):

    print(f"\nERROR: Image not found -> {IMAGE_PATH}")

    exit()


# ==========================================
# LOAD IMAGE
# ==========================================

print("\nReading image...")

image = cv2.imread(
    IMAGE_PATH
)


# ==========================================
# CHECK IMAGE
# ==========================================

if image is None:

    print("\nERROR: Failed to read image!")

    exit()

print("Image loaded successfully!")


# ==========================================
# IMAGE PREPROCESSING
# ==========================================

print("\nPreprocessing image...")


# Resize image
image = cv2.resize(
    image,
    (224, 224)
)


# Convert to float32
image = image.astype(
    np.float32
)


# Normalize pixel values
image = image / 255.0


# Add batch dimension
image = np.expand_dims(
    image,
    axis=0
)

print("Preprocessing completed!")


# ==========================================
# GET MODEL INPUT NAME
# ==========================================

input_name = session.get_inputs()[0].name


# ==========================================
# RUN MODEL PREDICTION
# ==========================================

print("\nRunning AI prediction...")


result = session.run(

    None,

    {

        input_name: image

    }

)


# ==========================================
# GET PREDICTION INDEX
# ==========================================

prediction_index = np.argmax(
    result[0]
)


# ==========================================
# GET PREDICTED CLASS
# ==========================================

predicted_class = CLASS_NAMES[
    prediction_index
]


# ==========================================
# GET CONFIDENCE SCORE
# ==========================================

confidence_score = float(

    np.max(result[0]) * 100

)


# ==========================================
# DISPLAY RESULT
# ==========================================

print("\n===================================")

print("ONION DISEASE PREDICTION RESULT")

print("===================================")

print(f"\nPredicted Disease : {predicted_class}")

print(f"Confidence Score  : {confidence_score:.2f}%")

print("\n===================================")