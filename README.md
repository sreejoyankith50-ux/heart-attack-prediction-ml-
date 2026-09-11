# 🫀 CardioCare AI — Heart Disease Prediction Web App

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

An end-to-end Machine Learning web application designed to predict the risk of cardiovascular disease (heart stroke / heart attack) based on routine clinical biomarkers. Powered by **Scikit-Learn's Logistic Regression** and an interactive **Streamlit** dashboard.

---

## 🖥️ Application Preview

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  🫀 CardioCare Diagnostic Assistant                                         │
│  Intelligent Cardiovascular Risk Assessment System                           │
└──────────────────────────────────────────────────────────────────────────────┘

  ┌── 👤 Patient Demographics ──────┐     ┌── 🩺 Cardiac Stress Metrics ────────┐
  │ • Age (years):               48 │     │ • Chest Pain:      ASY (Asymptomatic│
  │ • Biological Sex:          Male │     │ • Resting ECG:               Normal │
  │ • Resting BP:        125 mm Hg  │     │ • Max Heart Rate:           145 bpm │
  │ • Cholesterol:       210 mg/dL  │     │ • Exercise Angina:               No │
  │ • Fasting Sugar:   ≤ 120 mg/dL  │     │ • ST Depression (Oldpeak):      1.0 │
  │                                 │     │ • ST Slope:               Upsloping │
  └─────────────────────────────────┘     └─────────────────────────────────────┘

                       [ 🔍 Run Cardiovascular Assessment ]

  ┌─────────────────────────────────────────────────────────────────────────────┐
  │  📊 Evaluation Result:                                                      │
  │  • Status:       ✅ Low Risk of Heart Disease Detected                      │
  │  • Risk Score:   18.4% (Normal / Healthy Threshold)                         │
  │  • Action:       Routine annual physical exam & active cardio lifestyle     │
  └─────────────────────────────────────────────────────────────────────────────┘
```

---

## ✨ Highlights

- **Real-Time Risk Scoring:** Generates instant clinical prediction along with estimated risk probability percentage.
- **Modern Clinical UI:** Clean two-column layout with descriptive medical terms instead of confusing raw codes.
- **Normalized ML Pipeline:** One-hot encoding alignment and feature standardization via pre-trained `StandardScaler`.
- **Lightweight:** Entire model bundle is under 5 KB, requiring no GPU and running seamlessly on free cloud tiers.

---

## 🩺 Clinical Biomarkers Analyzed

| Feature | Description | Range / Values |
| :--- | :--- | :--- |
| **Age** | Age of the patient | 18 – 100 years |
| **Sex** | Biological sex | `Male`, `Female` |
| **Chest Pain Type** | Type of chest discomfort experienced | `ATA` (Atypical), `NAP` (Non-Anginal), `TA` (Typical), `ASY` (Asymptomatic) |
| **Resting BP** | Resting arterial blood pressure | 80 – 200 mm Hg |
| **Cholesterol** | Total serum cholesterol level | 100 – 600 mg/dL |
| **Fasting BS** | Fasting blood sugar | `> 120 mg/dL` (High), `≤ 120 mg/dL` (Normal) |
| **Resting ECG** | Resting electrocardiogram readings | `Normal`, `ST-T Abnormality`, `LVH` |
| **Max HR** | Maximum heart rate achieved during stress test | 60 – 220 bpm |
| **Exercise Angina** | Angina induced by physical exercise | `Yes`, `No` |
| **Oldpeak** | ST depression induced by exercise relative to rest | 0.0 – 6.0 mm |
| **ST Slope** | Slope of the peak exercise ST segment | `Upsloping`, `Flat`, `Downsloping` |

---

## 📁 Project Structure

```text
heart project/
│
├── .streamlit/
│   └── config.toml         # Streamlit UI theme and server configuration
├── models/
│   ├── Logistic_heart.pkl  # Pre-trained Logistic Regression model
│   ├── scaler.pkl          # Pre-fitted StandardScaler
│   └── columns.pkl         # Expected one-hot encoded feature list
├── app.py                  # Main Streamlit web application
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignored files
└── README.md               # Project documentation
```

---

## 🚀 Quickstart Guide

### 1. Clone or Download
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the Web App
```bash
streamlit run app.py
```
Your browser will open to `http://localhost:8501`.

---

## 📤 Upload Directly to GitHub

1. Create a **New Repository** on [GitHub.com](https://github.com/).
2. Leave *"Add a README"* and *".gitignore"* **unchecked**.
3. Click **"uploading an existing file"**.
4. Drag and drop:
   - `models/` (entire folder)
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
   - `.streamlit/`
5. Click **Commit changes**.

---

## ☁️ 1-Click Free Cloud Deployment

1. Push this repository to GitHub.
2. Visit **[share.streamlit.io](https://share.streamlit.io/)** and sign in with GitHub.
3. Click **New app** → select your repo → set main file to `app.py`.
4. Click **Deploy!** Your web app is live on the internet with a public link.

---

## ⚠️ Medical Disclaimer

This project is created strictly for **educational, demonstration, and research purposes**. It is not a certified medical device and should not be used as a substitute for professional clinical diagnosis or medical consultation.
