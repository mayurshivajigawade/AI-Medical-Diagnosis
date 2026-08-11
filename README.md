# 🩺 AI Medical Diagnosis Assistant

An AI-powered web application that detects **Pneumonia** from Chest X-ray images using **Deep Learning (CNN)**.

---

## Features

- Chest X-ray upload
- Pneumonia detection
- Confidence score
- Prediction history (SQLite)
- Professional Flask UI
- Image preview
- Responsive design

---

## Tech Stack

- Python
- TensorFlow / Keras
- Flask
- SQLite
- HTML
- CSS
- JavaScript

---

## Project Structure

```
AI-Medical-Diagnosis/
│
├── app.py
├── train.py
├── evaluate.py
├── predict.py
├── database.py
├── models/
├── templates/
├── static/
├── database/
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Medical-Diagnosis.git
```

Go to project folder

```bash
cd AI-Medical-Diagnosis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## AI Workflow

```
Chest X-ray

↓

Image Preprocessing

↓

CNN

↓

Prediction

↓

Confidence Score

↓

Result
```

---

## Future Improvements

- Grad-CAM
- Doctor Login
- Cloud Deployment
- Transfer Learning
- Multi-class Disease Detection

---

## Disclaimer

This project is intended for educational purposes only and should not be used as a substitute for professional medical diagnosis.