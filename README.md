# TruthGuard AI 🛡️  
### Hybrid Fake News Detection & Explainable AI Analysis System

TruthGuard AI is an AI-powered web application that detects fake news articles using Machine Learning and enhances prediction transparency using Generative AI.  

The system combines traditional supervised ML models with Gemini 2.5 Flash to provide credibility classification along with detailed explainable analysis.

---

## 🚀 Features

- 🧠 Machine Learning-based Fake News Detection
- 📊 TF-IDF Text Vectorization
- 🌲 Random Forest (Best Performing Model)
- 📈 Precision, Recall, F1 Score Evaluation
- 📄 PDF Upload Support
- 🖼 Image Upload with OCR (Tesseract)
- 🤖 Gemini 2.5 Flash AI Analysis
- 🔍 Bias & Misinformation Detection
- 📋 Fact-check Suggestions
- 🌐 Flask Web Application

---

## 🏗️ System Architecture

User Upload (PDF/Image)  
↓  
Text Extraction (PyPDF2 / OCR)  
↓  
Text Preprocessing  
↓  
TF-IDF Vectorization  
↓  
Random Forest Classification  
↓  
Confidence Score  
↓  
Gemini AI Explainable Analysis  
↓  
Result Displayed on Web Interface  

---

## 🧠 Machine Learning Models Used

- Logistic Regression  
- Multinomial Naive Bayes  
- Linear SVM  
- K-Nearest Neighbors  
- Random Forest (Final Selected Model)

### ✅ Best Model:
Random Forest  
- High Accuracy  
- Balanced Precision & Recall  
- Strong F1 Score  

---

## 📊 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score

F1 Score was prioritized to handle class imbalance effectively.

---

## 🤖 Generative AI Integration

Model Used:
`models/gemini-2.5-flash`

AI provides:

- Article Summary
- Misleading Content Detection
- Emotional Bias Analysis
- Suspicious Claims Identification
- Fact-Checking Suggestions

This enables Explainable AI (XAI) integration.

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- Flask
- PyPDF2
- Pytesseract OCR
- Google Gemini API (2.5 Flash)
- HTML/CSS
- Joblib

---

## 📂 Project Structure
# TruthGuard AI 🛡️  
### Hybrid Fake News Detection & Explainable AI Analysis System

TruthGuard AI is an AI-powered web application that detects fake news articles using Machine Learning and enhances prediction transparency using Generative AI.  

The system combines traditional supervised ML models with Gemini 2.5 Flash to provide credibility classification along with detailed explainable analysis.

---

## 🚀 Features

- 🧠 Machine Learning-based Fake News Detection
- 📊 TF-IDF Text Vectorization
- 🌲 Random Forest (Best Performing Model)
- 📈 Precision, Recall, F1 Score Evaluation
- 📄 PDF Upload Support
- 🖼 Image Upload with OCR (Tesseract)
- 🤖 Gemini 2.5 Flash AI Analysis
- 🔍 Bias & Misinformation Detection
- 📋 Fact-check Suggestions
- 🌐 Flask Web Application

---

## 🏗️ System Architecture

User Upload (PDF/Image)  
↓  
Text Extraction (PyPDF2 / OCR)  
↓  
Text Preprocessing  
↓  
TF-IDF Vectorization  
↓  
Random Forest Classification  
↓  
Confidence Score  
↓  
Gemini AI Explainable Analysis  
↓  
Result Displayed on Web Interface  

---

## 🧠 Machine Learning Models Used

- Logistic Regression  
- Multinomial Naive Bayes  
- Linear SVM  
- K-Nearest Neighbors  
- Random Forest (Final Selected Model)

### ✅ Best Model:
Random Forest  
- High Accuracy  
- Balanced Precision & Recall  
- Strong F1 Score  

---

## 📊 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score

F1 Score was prioritized to handle class imbalance effectively.

---

## 🤖 Generative AI Integration

Model Used:
`models/gemini-2.5-flash`

AI provides:

- Article Summary
- Misleading Content Detection
- Emotional Bias Analysis
- Suspicious Claims Identification
- Fact-Checking Suggestions

This enables Explainable AI (XAI) integration.

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- Flask
- PyPDF2
- Pytesseract OCR
- Google Gemini API (2.5 Flash)
- HTML/CSS
- Joblib

---

## 📂 Project Structure
TruthGuard-AI/
│
├── app.py
├── best_model.pkl
├── vectorizer.pkl
├── templates/
│ ├── index.html
│ └── result.html
├── static/
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
git clone https://github.com/vivek0323/AI-Fake-News-Detection.git

cd AI-Fake-News-Detection

---

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

---

### 3️⃣ Install Dependencies
pip install -r requirements.txt

---

### 4️⃣ Install Tesseract OCR (For Image Support)

Download from:
https://github.com/UB-Mannheim/tesseract/wiki

Set path in app.py:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

---

### 5️⃣ Add Gemini API Key

Replace in app.py:
API_KEY = "YOUR_API_KEY"

---

### 6️⃣ Run Application
python app.py

The browser will open automatically at:
http://127.0.0.1:5000

---

## 🎯 Why This Project is Unique

- Combines ML + LLM
- Provides Explainable AI output
- Supports real-world document input
- Industry-style deployment
- Production-ready pipeline

---

## 🔮 Future Enhancements

- Confusion Matrix Visualization
- SHAP Explainability
- Cloud Deployment (Render/Railway)
- Real-time News URL Scraper
- User History Tracking
- API Version of the Model

---

## 👨‍💻 Author

Vivek G  
B.Tech Computer Science & Engineering  
AI/ML Enthusiast  

GitHub: https://github.com/vivek0323  

---

## 📜 License

This project is for educational and research purposes.
