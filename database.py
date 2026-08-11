import sqlite3
import os
from datetime import datetime

# ==========================================
# Database Configuration
# ==========================================

DATABASE_FOLDER = "database"
DATABASE_NAME = "medical_ai.db"
DATABASE_PATH = os.path.join(
    DATABASE_FOLDER,
    DATABASE_NAME
)

# Create database folder automatically
os.makedirs(DATABASE_FOLDER, exist_ok=True)

# ==========================================
# Create Database
# ==========================================

def init_db():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            image_name TEXT NOT NULL,

            prediction TEXT NOT NULL,

            confidence REAL NOT NULL,

            prediction_time TEXT NOT NULL

        )
    """)

    connection.commit()

    connection.close()


# ==========================================
# Save Prediction
# ==========================================

def save_prediction(
    image_name,
    prediction,
    confidence
):

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute("""

        INSERT INTO predictions (

            image_name,
            prediction,
            confidence,
            prediction_time

        )

        VALUES (?, ?, ?, ?)

    """, (

        image_name,
        prediction,
        confidence,
        current_time

    ))

    connection.commit()

    connection.close()


# ==========================================
# Get Prediction History
# ==========================================

def get_history():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""

        SELECT
            id,
            image_name,
            prediction,
            confidence,
            prediction_time

        FROM predictions

        ORDER BY id DESC

    """)

    rows = cursor.fetchall()

    connection.close()

    return rows


# ==========================================
# Delete One Record
# ==========================================

def delete_prediction(record_id):

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute(

        "DELETE FROM predictions WHERE id=?",

        (record_id,)

    )

    connection.commit()

    connection.close()


# ==========================================
# Delete All Records
# ==========================================

def clear_history():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute(

        "DELETE FROM predictions"

    )

    connection.commit()

    connection.close()


# ==========================================
# Total Predictions
# ==========================================

def total_predictions():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute(

        "SELECT COUNT(*) FROM predictions"

    )

    count = cursor.fetchone()[0]

    connection.close()

    return count


# ==========================================
# Total Pneumonia Cases
# ==========================================

def total_pneumonia():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""

        SELECT COUNT(*)

        FROM predictions

        WHERE prediction='PNEUMONIA'

    """)

    count = cursor.fetchone()[0]

    connection.close()

    return count


# ==========================================
# Total Normal Cases
# ==========================================

def total_normal():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""

        SELECT COUNT(*)

        FROM predictions

        WHERE prediction='NORMAL'

    """)

    count = cursor.fetchone()[0]

    connection.close()

    return count