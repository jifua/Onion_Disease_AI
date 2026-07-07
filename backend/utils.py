# ==========================================
# IMPORT LIBRARIES
# ==========================================

import importlib
import importlib.util

for package in ("onnxruntime", "numpy", "cv2"):
    if importlib.util.find_spec(package) is None:
        raise ImportError(
            f"Missing required package '{package}'. Install with: pip install onnxruntime numpy opencv-python"
        )

ort = importlib.import_module("onnxruntime")
np = importlib.import_module("numpy")
cv2 = importlib.import_module("cv2")


# ==========================================
# LOAD AI MODEL
# ==========================================

session = ort.InferenceSession(
    "model/onion_disease_model2.onnx"
)


# ==========================================
# CLASS LABELS
# ==========================================

classes = [

    "Alternaria_D",

    "Caterpillar-P",

    "Fusarium-D",

    "Healthy leaves",

    "Iris yellow virus_augment",

    "Purple blotch",

    "Stemphylium Leaf Blight",

    "Viriosis-D"

]


# ==========================================
# PREDICT DISEASE FUNCTION
# ==========================================

def predict_disease(image_bytes):


    try:

        # ==================================
        # CONVERT IMAGE TO NUMPY
        # ==================================

        npimg = np.frombuffer(
            image_bytes,
            np.uint8
        )


        # ==================================
        # DECODE IMAGE
        # ==================================

        image = cv2.imdecode(
            npimg,
            cv2.IMREAD_COLOR
        )


        # ==================================
        # CHECK IMAGE
        # ==================================

        if image is None:

            return {

                "success": False,

                "error": "Image cannot be read"

            }


        # ==================================
        # RESIZE IMAGE
        # ==================================

        image = cv2.resize(
            image,
            (224, 224)
        )


        # ==================================
        # NORMALIZATION
        # ==================================

        image = image.astype(
            np.float32
        ) / 255.0


        # ==================================
        # ADD BATCH DIMENSION
        # ==================================

        image = np.expand_dims(
            image,
            axis=0
        )


        # ==================================
        # GET MODEL INPUT NAME
        # ==================================

        input_name = session.get_inputs()[0].name


        # ==================================
        # RUN AI MODEL
        # ==================================

        result = session.run(

            None,

            {

                input_name: image

            }

        )


        # ==================================
        # GET PREDICTION INDEX
        # ==================================

        pred_index = np.argmax(
            result[0]
        )


        # ==================================
        # GET CLASS NAME
        # ==================================

        prediction = classes[
            pred_index
        ]


        # ==================================
        # GET CONFIDENCE SCORE
        # ==================================

        confidence = float(

            np.max(result[0]) * 100

        )


        # ==================================
        # RETURN RESULT
        # ==================================

        return {

            "success": True,

            "prediction": prediction,

            "confidence": round(
                confidence,
                2
            )

        }


    except Exception as e:


        # ==================================
        # RETURN ERROR
        # ==================================

        return {

            "success": False,

            "error": str(e)

        }