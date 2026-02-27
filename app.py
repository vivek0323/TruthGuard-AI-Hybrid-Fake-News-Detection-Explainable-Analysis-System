import os
import joblib
import PyPDF2
from PIL import Image
import pytesseract
from flask import Flask, render_template, request
import threading
import webbrowser
from google import genai

# ==============================
# CONFIGURATION
# ==============================

# Set Tesseract Path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 🔐 PUT YOUR WORKING API KEY HERE
API_KEY = "AIzaSyA_UC4S9LRJVXKo1DtVgB6zxl2gaHqKkxc"

# Initialize Gemini Client (NEW SDK)
client = genai.Client(api_key=API_KEY)

app = Flask(__name__)

# ==============================
# Load ML Model
# ==============================
model = joblib.load("best_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ==============================
# PDF Text Extraction
# ==============================
def extract_text_from_pdf(file):
    try:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()
        return text
    except Exception as e:
        print("PDF Extraction Error:", e)
        return ""

# ==============================
# Image OCR Extraction
# ==============================
def extract_text_from_image(file):
    try:
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print("Image OCR Error:", e)
        return ""

# ==============================
# Routes
# ==============================
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("file")

    if not file:
        return "No file uploaded.", 400

    filename = file.filename.lower()

    # Extract text
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file)
    elif filename.endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".gif")):
        text = extract_text_from_image(file)
    else:
        return "Unsupported file format. Upload PDF or Image.", 400

    if not text.strip():
        return "Could not extract text from file.", 400

    # ==============================
    # ML Prediction
    # ==============================
    try:
        vectorized_text = vectorizer.transform([text])
        prediction = model.predict(vectorized_text)[0]
        confidence = model.predict_proba(vectorized_text)[0].max() * 100

        result = "REAL" if prediction == 1 else "FAKE"
    except Exception as e:
        print("ML Prediction Error:", e)
        return "Error processing article.", 500

    # ==============================
    # Gemini AI Analysis
    # ==============================
    prompt = f"""
Analyze this news article carefully:

1. Summary (3-4 lines)
2. Misleading elements
3. Emotional bias detection
4. Suspicious claims
5. Fact-check suggestions

Article:
{text[:3000]}
"""

    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )

        ai_text = response.text

    except Exception as e:
        print("Gemini Error:", e)
        ai_text = f"Gemini Error: {str(e)}"

    return render_template(
        "result.html",
        prediction=result,
        confidence=round(confidence, 2),
        ai_text=ai_text,
        filename=filename
    )

# ==============================
# Auto Open Browser
# ==============================
def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True, use_reloader=False)