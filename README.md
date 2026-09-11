# 🫀 Heart Disease Prediction Web App

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)]()

An end-to-end Machine Learning web application designed to predict the risk of cardiovascular disease (heart stroke / heart attack) based on clinical biometric data and patient health parameters. Powered by **Scikit-Learn's Logistic Regression** and deployed through an interactive **Streamlit** dashboard.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Biomarkers & Clinical Features](#-biomarkers--clinical-features)
- [Project Architecture](#-project-architecture)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [How to Upload to GitHub](#-how-to-upload-to-github)
- [Free Cloud Deployment](#-free-cloud-deployment)
- [Machine Learning Workflow](#-machine-learning-workflow)
- [Medical Disclaimer](#-medical-disclaimer)
- [License](#-license)

---

## 📖 Overview

Cardiovascular diseases (CVDs) are one of the leading causes of mortality worldwide. Early identification of high-risk patients can substantially reduce mortality rates by facilitating early medical interventions. 

This project implements a complete binary classification pipeline trained on standard clinical parameters (such as blood pressure, cholesterol levels, resting ECG, and exercise-induced angina). A pre-trained, normalized **Logistic Regression** model classifies incoming patient metrics into **High Risk** or **Low Risk**.

---

## ✨ Key Features

- **Instant Clinical Evaluation:** Real-time risk prediction with immediate visual feedback (Low Risk / High Risk).
- **Interactive Web Interface:** Intuitive UI built using Streamlit with sliders, select boxes, and numerical inputs.
- **Robust Preprocessing Pipeline:** Automated one-hot encoding alignment and feature scaling using a pre-fitted `StandardScaler`.
- **Lightweight & Portable:** Compact model artifacts (`.pkl`) under 5 KB total, easily deployable to any cloud platform with no external GPU required.
- **Platform Agnostic:** Implements dynamic relative paths for error-free deployment on Windows, Linux, macOS, and containerized cloud environments.

---

## 🩺 Biomarkers & Clinical Features

The model analyzes 11 critical clinical biomarkers:

| Feature | Description | Values / Range |
| :--- | :--- | :--- |
| **Age** | Age of the patient | 18 – 100 years |
| **Sex** | Biological sex of the patient | `M` (Male), `F` (Female) |
| **Chest Pain Type** | Type of chest discomfort experienced | `ATA` (Atypical Angina), `NAP` (Non-Anginal Pain), `TA` (Typical Angina), `ASY` (Asymptomatic) |
| **Resting BP** | Resting blood pressure | 80 – 200 mm Hg |
| **Cholesterol** | Serum cholesterol level | 100 – 600 mg/dL |
| **Fasting BS** | Fasting blood sugar level | `1` if Fasting BS > 120 mg/dl, `0` otherwise |
| **Resting ECG** | Resting electrocardiogram results | `Normal`, `st` (ST-T wave abnormality), `lvh` (Left ventricular hypertrophy) |
| **Max HR** | Maximum heart rate achieved | 60 – 220 bpm |
| **Exercise Angina** | Exercise-induced angina | `Y` (Yes), `N` (No) |
| **Oldpeak** | ST depression induced by exercise relative to rest | 0.0 – 6.0 |
| **ST Slope** | Slope of the peak exercise ST segment | `UP` (Upsloping), `Flat`, `Down` (Downsloping) |

---

## 📁 Project Architecture

```text
├── .streamlit/
│   └── config.toml         # Streamlit theme & UI configurations
├── models/
│   ├── Logistic_heart.pkl  # Pre-trained Logistic Regression model
│   ├── scaler.pkl          # Pre-fitted StandardScaler
│   └── columns.pkl         # Serialized feature list for encoding
├── app.py                  # Main Streamlit web application script
├── requirements.txt        # Python dependency specifications
├── .gitignore              # Files and patterns ignored by Git
├── LICENSE                 # MIT License file
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

Follow these steps to run the application locally on your machine.

### Prerequisites

- **Python 3.8** or higher installed ([Download Python](https://www.python.org/downloads/))
- **Git** installed ([Download Git](https://git-scm.com/))

### Installation

1. **Clone or download the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
   cd YOUR_REPOSITORY_NAME
   ```

2. **Create a virtual environment (Recommended):**
   - **Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

Start the Streamlit development server:

```bash
streamlit run app.py
```

After running the command, your web browser should automatically open to:
```text
http://localhost:8501
```

---

## 📤 How to Upload to GitHub

If you are uploading these files manually or via the command line:

### Option A: Via GitHub Website (Direct Upload)
1. Go to [GitHub](https://github.com/) and click **New Repository**.
2. Name your repository (e.g., `heart-disease-prediction`).
3. Leave "Add a README" and ".gitignore" **unchecked** (since you already have them).
4. Click **Create repository**.
5. In your new repository page, click **uploading an existing file**.
6. Drag and drop the project contents into the browser:
   - `models/` (entire folder)
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
   - `LICENSE`
   - `.streamlit/` (optional theme folder)
7. Click **Commit changes**.

### Option B: Via Terminal / Command Line
```bash
git init
git add .
git commit -m "Initial commit: Heart disease prediction ML application"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
git push -u origin main
```

---

## ☁️ Free Cloud Deployment

### Deploy on Streamlit Community Cloud (Recommended)
1. Push your repository to GitHub.
2. Visit [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
3. Click **New app**.
4. Select your repository, set the branch to `main`, and main file path to `app.py`.
5. Click **Deploy!** Your app will be live on the internet with a shareable URL in less than 2 minutes.

---

## 🧠 Machine Learning Workflow

1. **Data Ingestion & Alignment:** User inputs are collected via Streamlit widgets and placed into a dictionary structure.
2. **One-Hot Encoding Alignment:** The input is matched against `columns.pkl` ensuring that unseen categorical columns are initialized to 0 and all columns follow the exact training order.
3. **Standardization:** Continuous numerical features and aligned columns are scaled using `scaler.pkl` (`StandardScaler.transform`).
4. **Inference:** The scaled feature array is passed to `Logistic_heart.pkl` (`model.predict`), outputting the binary clinical classification:
   - `0`: **Low risk of heart disease**
   - `1`: **High risk of heart disease**

---

## ⚠️ Medical Disclaimer

> **IMPORTANT:** This software application and machine learning model are created for **educational, demonstration, and research purposes only**. It is **not** a certified medical diagnostic device and must not be used as a substitute for professional medical advice, clinical diagnosis, or treatment. Always consult a certified healthcare professional for medical evaluations.

---

## 📜 License

This project is open-source and distributed under the [MIT License](LICENSE).
