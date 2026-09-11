# 🫀 Heart Disease Prediction using Logistic Regression

A Machine Learning web application built with **Python**, **Scikit-Learn**, and **Streamlit** to predict heart disease risk based on patient health details.

---

## 🖥️ App Preview

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  🫀 Heart Disease Prediction                                                 │
│  Provide the patient details to check heart disease risk                     │
└──────────────────────────────────────────────────────────────────────────────┘

  ┌── 👤 Patient Details ───────────┐     ┌── 🩺 Health & Heart Tests ──────────┐
  │ • Age:                       45 │     │ • Chest Pain Type:              ASY │
  │ • Sex:                     Male │     │ • Resting ECG:               Normal │
  │ • Resting BP:        120 mm Hg  │     │ • Max Heart Rate:           150 bpm │
  │ • Cholesterol:       200 mg/dL  │     │ • Exercise Angina:               No │
  │ • Fasting Sugar:     ≤ 120 mg/dL│     │ • Oldpeak (ST Depression):      1.0 │
  │                                 │     │ • ST Slope:               Upsloping │
  └─────────────────────────────────┘     └─────────────────────────────────────┘

                            [ 🔍 Predict Risk ]

  ┌─────────────────────────────────────────────────────────────────────────────┐
  │  📊 Result:                                                                 │
  │  • Prediction:   Low Risk of Heart Disease                                  │
  │  • Probability:  18.4%                                                      │
  └─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🩺 Inputs Explained

| Input | Meaning | Options / Normal Values |
| :--- | :--- | :--- |
| **Age** | Age in years | 18 to 100 |
| **Sex** | Gender | Male (`M`) or Female (`F`) |
| **Chest Pain Type** | Type of chest pain | `ATA` (Atypical), `NAP` (Non-anginal), `TA` (Typical), `ASY` (Asymptomatic) |
| **Resting BP** | Blood pressure at rest | Normal is around 120 mm Hg |
| **Cholesterol** | Serum cholesterol | Normal is around 200 mg/dL |
| **Fasting BS** | Fasting blood sugar > 120 | `0` (No / Normal) or `1` (Yes / High) |
| **Resting ECG** | ECG test results | `Normal`, `st` (ST-T abnormality), `lvh` (Left ventricular hypertrophy) |
| **Max HR** | Highest heart rate during exercise | 60 to 220 bpm |
| **Exercise Angina** | Chest pain caused by exercise | `Y` (Yes) or `N` (No) |
| **Oldpeak** | ST depression on ECG | 0.0 to 6.0 |
| **ST Slope** | Slope of peak exercise ST segment | `UP` (Upsloping), `Flat`, `Down` (Downsloping) |

---

## 📁 Project Structure

```text
heart project/
│
├── .streamlit/
│   └── config.toml         # Streamlit styling settings
├── models/
│   ├── Logistic_heart.pkl  # Trained Logistic Regression model
│   ├── scaler.pkl          # Feature scaler
│   └── columns.pkl         # Expected columns list
├── app.py                  # Main web app code
├── requirements.txt        # Required Python libraries
├── .gitignore              # Files git should ignore
└── README.md               # Project documentation
```

---

## 🚀 How to Run the Project Locally

1. Open your terminal or command prompt in this folder.
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. It will automatically open in your browser at `http://localhost:8501`.

---

## 📤 How to Upload to GitHub

1. Go to [GitHub.com](https://github.com/) and create a **New repository**.
2. Click **uploading an existing file**.
3. Drag and drop all these files into GitHub:
   - `models/` folder
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
   - `.streamlit/` folder
4. Click **Commit changes**.
