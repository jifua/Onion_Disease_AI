# ==========================================
# IMPORT FASTAPI
# ==========================================

from fastapi import FastAPI, File, UploadFile  # type: ignore


# ==========================================
# IMPORT AI UTILITIES
# ==========================================

from backend.utils import predict_disease


# ==========================================
# CREATE FASTAPI APPLICATION
# ==========================================

app = FastAPI(

    title="Onion Disease Detection API",

    description=
    """
    AI-powered onion disease classification
    using ONNX Runtime and FastAPI.
    """,

    version="1.0.0"

)


# ==========================================
# HOME ROUTE
# ==========================================

@app.get("/")

async def home():

    """
    API Home Endpoint
    """

    return {

        "message":
        "Onion Disease Detection API is running"

    }


# ==========================================
# AI PREDICTION ROUTE
# ==========================================

@app.post("/predict")

async def predict(

    file: UploadFile = File(...)

):

    """
    Upload image and predict onion disease
    using ONNX AI model.
    """


    # ======================================
    # READ IMAGE FILE
    # ======================================

    image_bytes = await file.read()


    # ======================================
    # RUN AI PREDICTION
    # ======================================

    prediction_result = predict_disease(
        image_bytes
    )


    # ======================================
    # RETURN ERROR
    # ======================================

    if not prediction_result["success"]:

        return {

            "success": False,

            "error":
            prediction_result["error"]

        }


    # ======================================
    # RETURN SUCCESS RESULT
    # ======================================

    return {

        "success": True,

        "filename": file.filename,

        "prediction":
        prediction_result["prediction"],

        "confidence":
        prediction_result["confidence"]

    }