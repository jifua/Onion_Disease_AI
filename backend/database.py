# ==========================================
# IMPORT LIBRARY
# ==========================================

import sqlite3

from datetime import datetime


# ==========================================
# DATABASE NAME
# ==========================================

DATABASE_NAME = "prediction_history.db"


# ==========================================
# CREATE DATABASE TABLE
# ==========================================

def create_table():
    """
    Membuat tabel prediction_history
    jika belum tersedia
    """

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prediction_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        image_path TEXT,

        prediction TEXT,

        confidence REAL,

        created_at TEXT
    )
    """)

    connection.commit()

    connection.close()


# ==========================================
# SAVE PREDICTION RESULT
# ==========================================

def save_prediction(
    image_path,
    prediction,
    confidence
):
    """
    Menyimpan hasil prediksi AI
    ke database SQLite
    """

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute("""
    INSERT INTO prediction_history (
        image_path,
        prediction,
        confidence,
        created_at
    )

    VALUES (?, ?, ?, ?)
    """, (
        image_path,
        prediction,
        confidence,
        current_time
    ))

    connection.commit()

    connection.close()


# ==========================================
# GET ALL HISTORY
# ==========================================

def get_prediction_history():
    """
    Mengambil seluruh history prediksi
    dari database
    """

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM prediction_history
    ORDER BY id DESC
    """)

    history_data = cursor.fetchall()

    connection.close()

    return history_data


# ==========================================
# TOTAL PREDICTIONS
# ==========================================

def get_total_predictions():
    """
    Menghitung total prediksi
    """

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM prediction_history
    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total


# ==========================================
# AVERAGE CONFIDENCE
# ==========================================

def get_average_confidence():
    """
    Menghitung rata-rata confidence
    """

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
    SELECT AVG(confidence)
    FROM prediction_history
    """)

    result = cursor.fetchone()[0]

    connection.close()

    if result is None:
        return 0

    return round(result, 2)


# ==========================================
# MOST COMMON DISEASE
# ==========================================

def get_most_common_disease():
    """
    Mengambil penyakit
    yang paling sering terdeteksi
    """

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
    SELECT prediction,
           COUNT(prediction) as total

    FROM prediction_history

    GROUP BY prediction

    ORDER BY total DESC

    LIMIT 1
    """)

    result = cursor.fetchone()

    connection.close()

    if result is None:
        return "No Data"

    return result[0]

# =========================================
# USER TABLE
# =========================================

def create_user_table():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        password TEXT

    )

    """)

    conn.commit()

    conn.close()

# =========================================
# REGISTER USER
# =========================================

def register_user(username, password):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    try:

        cursor.execute(

            "INSERT INTO users (username, password) VALUES (?, ?)",

            (username, password)

        )

        conn.commit()

        return True

    except Exception:

        return False

    finally:

        conn.close()

# =========================================
# LOGIN USER
# =========================================

def login_user(username, password):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM users WHERE username=? AND password=?",

        (username, password)

    )

    user = cursor.fetchone()

    conn.close()

    return user

# =========================================
# DATABASE NAME
# =========================================

DB_NAME = "prediction_history.db"