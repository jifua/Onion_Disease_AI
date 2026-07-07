# ==========================================
# IMPORT LIBRARIES
# ==========================================

import os

from fastapi import FastAPI, Request, UploadFile, File, Form  # type: ignore[import]
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse # type: ignore[import]
from fastapi.staticfiles import StaticFiles  # type: ignore[import]
from fastapi.templating import Jinja2Templates  # type: ignore[import]
from backend.chatbot import get_ai_response

# ==========================================
# IMPORT AI PREDICTION SYSTEM
# ==========================================

from backend.utils import predict_disease

# ==========================================
# IMPORT DATABASE SYSTEM
# ==========================================

from backend.database import (

    create_table,
    save_prediction,
    get_prediction_history,
    get_total_predictions,
    get_average_confidence,
    get_most_common_disease,

    create_user_table,
    register_user,
    login_user

)

# ==========================================
# IMPORT KNOWLEDGE BASE
# ==========================================

from backend.disease_info import DISEASE_INFO

# ==========================================
# CREATE FASTAPI APP
# ==========================================

app = FastAPI(

    title="Onion Disease Detection AI",

    description=
    "AI-powered onion disease detection system",

    version="2.0.0"

)

# =========================================
# INITIALIZE DATABASE
# =========================================

create_table()

create_user_table()

# ==========================================
# CONNECT STATIC FILES
# ==========================================

app.mount(

    "/static",

    StaticFiles(directory="static"),

    name="static"

)

# ==========================================
# CONNECT ASSETS
# ==========================================

app.mount(

    "/assets",

    StaticFiles(directory="assets"),

    name="assets"

)

# ==========================================
# CONNECT UPLOADS
# ==========================================

app.mount(

    "/uploads",

    StaticFiles(directory="uploads"),

    name="uploads"

)

# ==========================================
# TEMPLATE ENGINE
# ==========================================

templates = Jinja2Templates(

    directory="templates"

)

# ==========================================
# HOME PAGE
# ==========================================

@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(

        "index.html",

        {

            "request": request

        }

    )

# ==========================================
# AI PREDICTION ROUTE
# ==========================================

@app.post("/predict")
async def predict(

    request: Request,

    file: UploadFile = File(...)

):

    try:

        # ==================================
        # VALIDASI FILE
        # ==================================

        if not file.filename:

            return templates.TemplateResponse(

                "index.html",

                {

                    "request": request,

                    "error":
                    "File gambar tidak ditemukan"

                }

            )

        # ==================================
        # CREATE UPLOAD DIRECTORY
        # ==================================

        os.makedirs(

            "uploads",

            exist_ok=True

        )

        # ==================================
        # SAVE FILE
        # ==================================

        file_location = f"uploads/{file.filename}"

        image_bytes = await file.read()

        with open(file_location, "wb") as f:

            f.write(image_bytes)

        # ==================================
        # RUN AI MODEL
        # ==================================

        result = predict_disease(image_bytes)

        # ==================================
        # HANDLE AI ERROR
        # ==================================

        if not result["success"]:

            return templates.TemplateResponse(

                "index.html",

                {

                    "request": request,

                    "error":
                    result["error"]

                }

            )

        # ==================================
        # GET AI RESULT
        # ==================================

        prediction = result.get(

            "prediction",

            "Unknown"

        )

        confidence = result.get(

            "confidence",

            0

        )

        # ==================================
        # GET KNOWLEDGE BASE
        # ==================================

        disease_data = DISEASE_INFO.get(

            prediction,

            {

                "display_name":
                "Penyakit Tidak Dikenali",

                "english_name":
                "Unknown Disease",

                "scientific_name":
                "-",

                "category":
                "Tidak Diketahui",

                "cause":
                "Sistem tidak menemukan data penyakit.",

                "symptoms":
                "Gejala belum tersedia.",

                "impact":
                "Belum tersedia.",

                "prevention":
                "Lakukan monitoring tanaman.",

                "solution":
                "Konsultasikan dengan ahli pertanian.",

                "pesticide":
                "-",

                "active_ingredient":
                "-",

                "usage":
                "-",

                "risk":
                "Tidak Diketahui",

                "notes":
                "Database penyakit akan terus diperbarui."

            }

        )

        # ==================================
        # SAVE HISTORY DATABASE
        # ==================================

        save_prediction(

            image_path=file.filename,

            prediction=prediction,

            confidence=confidence

        )

        # ==================================
        # RETURN RESULT
        # ==================================

        return templates.TemplateResponse(

            "index.html",

            {

                "request": request,

                "prediction": prediction,

                "confidence": confidence,

                "disease_data": disease_data,

                "uploaded_image":
                "/" + file_location

            }

        )

    except Exception as e:

        return templates.TemplateResponse(

            "index.html",

            {

                "request": request,

                "error":
                f"Terjadi kesalahan sistem AI: {str(e)}"

            }

        )

# ==========================================
# HISTORY PAGE
# ==========================================

@app.get("/history")
async def history_page(request: Request):

    history_data = get_prediction_history()

    return templates.TemplateResponse(

        "history.html",

        {

            "request": request,

            "rows": history_data

        }

    )

# ==========================================
# DASHBOARD PAGE
# ==========================================

@app.get("/dashboard")
async def dashboard_page(request: Request):

    total_predictions = get_total_predictions()

    average_confidence = get_average_confidence()

    most_common_disease = get_most_common_disease()

    if not most_common_disease:

        most_common_disease = "Belum Ada Data"

    return templates.TemplateResponse(

        "dashboard.html",

        {

            "request": request,

            "total_predictions":
            total_predictions,

            "average_confidence":
            average_confidence,

            "most_common_disease":
            most_common_disease

        }

    )

# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health")
async def health_check():

    return {

        "status": "online",

        "system":
        "Onion Disease Detection AI",

        "version":
        "2.0.0"

    }

# ==========================================
# ABOUT API
# ==========================================

@app.get("/about")
async def about_api():

    return {

        "project":
        "Onion Disease Detection AI",

        "developer":
        "AI Smart Agriculture System",

        "technology": [

            "FastAPI",
            "Deep Learning",
            "ONNX Runtime",
            "Computer Vision",
            "Artificial Intelligence"

        ],

        "purpose":
        "Membantu petani bawang merah mendeteksi penyakit menggunakan AI."

    }


# =========================================
# REGISTER PAGE
# =========================================

@app.get("/register")
async def register_page(request: Request):

    return templates.TemplateResponse(

        "register.html",

        {

            "request": request

        }

    )

# =========================================
# REGISTER USER
# =========================================

@app.post("/register")
async def register(

    request: Request,

    username: str = Form(...),

    password: str = Form(...)

):

    success = register_user(username, password)

    if success:

        return RedirectResponse(

            url="/login",

            status_code=303

        )

    return templates.TemplateResponse(

        "register.html",

        {

            "request": request,

            "error": "Username sudah digunakan"

        }

    )

# =========================================
# LOGIN PAGE
# =========================================

@app.get("/login")
async def login_page(request: Request):

    return templates.TemplateResponse(

        "login.html",

        {

            "request": request

        }

    )

# =========================================
# LOGIN USER
# =========================================

@app.post("/login")
async def login(

    request: Request,

    username: str = Form(...),

    password: str = Form(...)

):

    user = login_user(username, password)

    if user:

        return RedirectResponse(

            url="/",

            status_code=303

        )

    return templates.TemplateResponse(

        "login.html",

        {

            "request": request,

            "error": "Username atau password salah"

        }

    )

@app.get("/Chatbot", response_class=HTMLResponse)
async def Chatbot(request: Request):

    return templates.TemplateResponse(

        "Chatbot.html",

        {

            "request": request

        }

    )

# =========================================
# CHATBOT PAGE
# =========================================

@app.get("/chatbot", response_class=HTMLResponse)
async def chatbot_page(request: Request):

    return templates.TemplateResponse(
        "chatbot.html",
        {
            "request": request
        }
    )

# =========================================
# CHATBOT API
# =========================================

@app.post("/chatbot-api")
async def chatbot_api(data: dict):

    message = data.get("message", "")

    response = get_ai_response(message)

    return response

# =========================================================
# ONIONBOT CHAT API
# =========================================================


@app.post("/chat")
async def onionbot_chat(request: Request):

    data = await request.json()

    user_message = data.get("message", "")

    # IMPORT CHATBOT ENGINE
    from backend.chatbot import get_ai_response

    result = get_ai_response(user_message)

    return JSONResponse(content=result)