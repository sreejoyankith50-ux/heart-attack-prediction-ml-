# 🫀 Heart Disease Prediction Web App

A Machine Learning web application built with **Python**, **Scikit-Learn**, and **Streamlit** to predict heart disease risk based on patient health details and clinical biomarkers.

---

## 🖥️ App Preview

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  🫀 CardioCare Diagnostic Assistant                                         │
│  Provide the patient details to check heart disease risk                     │
└──────────────────────────────────────────────────────────────────────────────┘

  ┌── 👤 Patient Demographics ──────┐     ┌── 🩺 Cardiac Stress Metrics ────────┐
  │ • Age (years):               48 │     │ • Chest Pain:      ASY (Asymptomatic│
  │ • Biological Sex:          Male │     │ • Resting ECG:               Normal │
  │ • Resting BP:        125 mm Hg  │     │ • Max Heart Rate:           145 bpm │
  │ • Cholesterol:       210 mg/dL  │     │ • Exercise Angina:               No │
  │ • Fasting Sugar:     ≤ 120 mg/dL│     │ • ST Depression (Oldpeak):      1.0 │
  │                                 │     │ • ST Slope:               Upsloping │
  └─────────────────────────────────┘     └─────────────────────────────────────┘

                       [ 🔍 Run Risk Assessment ]

  ┌─────────────────────────────────────────────────────────────────────────────┐
  │  📊 Evaluation Result:                                                      │
  │  • Status:       Low Risk of Heart Disease Detected                         │
  │  • Risk Score:   18.4% (Healthy Threshold)                                  │
  │  • Action:       Routine annual physical exam & active cardio lifestyle     │
  └─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🩺 Inputs & Clinical Biomarkers

| Feature | Description | Values / Normal Range |
| :--- | :--- | :--- |
| **Age** | Age of the patient | 18 – 100 years |
| **Sex** | Biological sex | `M` (Male) or `F` (Female) |
| **Chest Pain Type** | Type of chest discomfort | `ATA` (Atypical), `NAP` (Non-Anginal), `TA` (Typical), `ASY` (Asymptomatic) |
| **Resting BP** | Resting blood pressure | 80 – 200 mm Hg (Normal ~120 mm Hg) |
| **Cholesterol** | Serum cholesterol | 100 – 600 mg/dL (Desirable < 200 mg/dL) |
| **Fasting BS** | Fasting blood sugar > 120 mg/dL | `0` (Normal / No) or `1` (High / Yes) |
| **Resting ECG** | Resting electrocardiogram readings | `Normal`, `st` (ST-T abnormality), `lvh` (Left ventricular hypertrophy) |
| **Max HR** | Highest heart rate achieved | 60 – 220 bpm |
| **Exercise Angina** | Angina induced by exercise | `Y` (Yes) or `N` (No) |
| **Oldpeak** | ST depression induced by exercise | 0.0 – 6.0 mm |
| **ST Slope** | Slope of peak exercise ST segment | `UP` (Upsloping), `Flat`, `Down` (Downsloping) |

---

## 📁 Project Structure

```text
heart project/
│
├── .streamlit/
│   └── config.toml         # Streamlit UI theme and styling configurations
├── models/
│   ├── Logistic_heart.pkl  # Trained Logistic Regression classification model
│   ├── scaler.pkl          # Pre-fitted StandardScaler for normalization
│   └── columns.pkl         # Expected one-hot encoded feature column list
├── app.py                  # Streamlit web application frontend & inference
├── requirements.txt        # Required Python packages
├── .gitignore              # Files ignored by version control
└── README.md               # Project documentation
```

---

## 🚀 How to Run

1. Clone or download this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
   cd YOUR_REPOSITORY_NAME
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the application:
   ```bash
   streamlit run app.py
   ```

The web app will open automatically in your browser at `http://localhost:8501`.
