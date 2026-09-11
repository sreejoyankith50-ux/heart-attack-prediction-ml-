from pathlib import Path
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="CardioCare AI | Heart Disease Risk Prediction",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" if (BASE_DIR / "models").exists() else BASE_DIR

@st.cache_resource
def load_artifacts():
    model = joblib.load(MODEL_DIR / "Logistic_heart.pkl")
    scaler = joblib.load(MODEL_DIR / "scaler.pkl")
    expected_columns = joblib.load(MODEL_DIR / "columns.pkl")
    return model, scaler, expected_columns

try:
    model, scaler, expected_columns = load_artifacts()
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"], [class*="st-"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .hero-banner {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0F172A 100%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 2.2rem 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.3);
    }
    .hero-badge {
        display: inline-block;
        background: rgba(239, 68, 68, 0.15);
        color: #F87171;
        border: 1px solid rgba(239, 68, 68, 0.3);
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 0.8rem;
    }
    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #FFFFFF;
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #94A3B8;
        margin: 0;
        line-height: 1.5;
        max-width: 800px;
    }

    .panel-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 1.6rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px -2px rgba(0, 0, 0, 0.04);
    }
    .panel-header {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A;
        border-bottom: 2px solid #F1F5F9;
        padding-bottom: 0.8rem;
        margin-bottom: 1.2rem;
    }

    .result-box-high {
        background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
        border: 1.5px solid #FCA5A5;
        border-left: 6px solid #EF4444;
        border-radius: 14px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .result-box-low {
        background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
        border: 1.5px solid #6EE7B7;
        border-left: 6px solid #10B981;
        border-radius: 14px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .result-title {
        font-size: 1.35rem;
        font-weight: 800;
        margin-bottom: 0.3rem;
    }
    .result-title-high { color: #991B1B; }
    .result-title-low { color: #065F46; }
    .result-desc {
        font-size: 0.95rem;
        color: #475569;
        line-height: 1.4;
    }

    div.stButton > button:first-child {
        background: linear-gradient(135deg, #E11D48 0%, #BE123C 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.3px !important;
        box-shadow: 0 4px 15px rgba(225, 29, 72, 0.35) !important;
        transition: all 0.25s ease-in-out !important;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(225, 29, 72, 0.5) !important;
        background: linear-gradient(135deg, #F43F5E 0%, #E11D48 100%) !important;
    }
    
    .chip {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 2px 4px 2px 0;
    }
    .chip-warn {
        background-color: #FEF3C7;
        color: #92400E;
        border: 1px solid #FCD34D;
    }
    .chip-ok {
        background-color: #DEF7EC;
        color: #03543F;
        border: 1px solid #84E1BC;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🫀 CardioCare AI")
    st.markdown("Clinical machine learning screening system designed to evaluate risk factors for cardiovascular disease.")
    st.markdown("---")
    
    st.markdown("#### ⚙️ Pipeline Specifications")
    st.markdown("- **Classifier:** Logistic Regression")
    st.markdown("- **Feature Scaler:** StandardScaler")
    st.markdown("- **Biomarkers:** 11 Clinical Parameters")
    st.markdown("- **Deployment:** Streamlit Web App")
    st.markdown("---")
    
    st.markdown("#### 📋 Reference Benchmarks")
    st.markdown("""
    - **Blood Pressure:** < 120 mm Hg (Optimal)
    - **Cholesterol:** < 200 mg/dL (Desirable)
    - **Fasting Sugar:** ≤ 120 mg/dL (Normal)
    - **Max Heart Rate:** 220 minus Patient Age
    """)
    st.markdown("---")
    
    st.info("⚠️ **Disclaimer:** For educational & demonstration purposes only. Not a medical device.")

st.markdown("""
<div class="hero-banner">
    <div class="hero-badge">Medical ML Screening System</div>
    <div class="hero-title">CardioCare Diagnostic Assistant</div>
    <div class="hero-subtitle">Evaluate cardiovascular and stroke risk in real-time by entering routine clinical biomarkers and exercise stress metrics.</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="panel-header">
        <span>👤</span> Patient Demographics & Baseline Vitals
    </div>
    """, unsafe_allow_html=True)
    
    age = st.slider("Age (years)", min_value=18, max_value=100, value=48, help="Patient age in years")
    
    sex = st.radio(
        "Biological Sex",
        options=['M', 'F'],
        format_func=lambda x: "Male (M)" if x == 'M' else "Female (F)",
        horizontal=True
    )
    
    restingbp = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        min_value=80,
        max_value=200,
        value=125,
        step=1,
        help="Resting arterial blood pressure measured in mm Hg"
    )
    
    cholesterol = st.number_input(
        "Serum Cholesterol (mg/dL)",
        min_value=100,
        max_value=600,
        value=210,
        step=5,
        help="Total serum cholesterol measured in mg/dL"
    )
    
    fasting_bs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dL",
        options=[0, 1],
        format_func=lambda x: "Yes (> 120 mg/dL - High / Diabetic risk)" if x == 1 else "No (≤ 120 mg/dL - Normal)"
    )

with col2:
    st.markdown("""
    <div class="panel-header">
        <span>🩺</span> Cardiac & Exercise Stress Metrics
    </div>
    """, unsafe_allow_html=True)
    
    chest_pain_labels = {
        'ASY': 'ASY — Asymptomatic',
        'NAP': 'NAP — Non-Anginal Pain',
        'ATA': 'ATA — Atypical Angina',
        'TA': 'TA — Typical Angina'
    }
    chest_pain = st.selectbox(
        "Chest Pain Type",
        options=['ASY', 'NAP', 'ATA', 'TA'],
        format_func=lambda x: chest_pain_labels.get(x, x)
    )
    
    ecg_labels = {
        'Normal': 'Normal',
        'st': 'ST — ST-T Wave Abnormality',
        'lvh': 'LVH — Left Ventricular Hypertrophy'
    }
    resting_ecg = st.selectbox(
        "Resting Electrocardiogram (ECG)",
        options=['Normal', 'st', 'lvh'],
        format_func=lambda x: ecg_labels.get(x, x)
    )
    
    max_hr = st.slider("Maximum Heart Rate Achieved (bpm)", min_value=60, max_value=220, value=145)
    
    exercise_angina = st.radio(
        "Exercise-Induced Angina",
        options=['N', 'Y'],
        format_func=lambda x: "Yes (Angina provoked during exercise)" if x == 'Y' else "No (None)",
        horizontal=True
    )
    
    oldpeak = st.slider(
        "ST Depression Induced by Exercise (Oldpeak)",
        min_value=0.0,
        max_value=6.0,
        value=1.0,
        step=0.1,
        help="Depression of the ST segment relative to rest (measured in mm)"
    )
    
    st_slope_labels = {
        'UP': 'Up — Upsloping',
        'Flat': 'Flat — Horizontal',
        'Down': 'Down — Downsloping'
    }
    st_slope = st.selectbox(
        "ST Slope at Peak Exercise",
        options=['UP', 'Flat', 'Down'],
        format_func=lambda x: st_slope_labels.get(x, x)
    )

st.markdown("<br>", unsafe_allow_html=True)
btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
with btn_col2:
    predict_clicked = st.button("🔍 Generate Cardiovascular Assessment", use_container_width=True)

if predict_clicked:
    raw_input = {
        'Age': age,
        'RestingBP': restingbp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }
    
    input_df = pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
            
    input_df = input_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    
    prediction = model.predict(scaled_input)[0]
    
    try:
        probabilities = model.predict_proba(scaled_input)[0]
        risk_probability = probabilities[1] * 100
    except Exception:
        risk_probability = None

    st.markdown("---")
    st.markdown("### 📊 Diagnostic Evaluation Results")
    
    res_col1, res_col2 = st.columns([1.2, 1], gap="large")
    
    with res_col1:
        if prediction == 1:
            st.markdown(f"""
            <div class="result-box-high">
                <div class="result-title result-title-high">⚠️ High Risk of Heart Disease Detected</div>
                <div class="result-desc">The predictive model evaluated the patient parameters and detected high risk markers associated with cardiovascular condition.</div>
            </div>
            """, unsafe_allow_html=True)
            
            if risk_probability is not None:
                mcol1, mcol2 = st.columns(2)
                with mcol1:
                    st.metric("Estimated Risk Probability", f"{risk_probability:.1f}%")
                with mcol2:
                    st.metric("Risk Classification", "Elevated", delta="Action Required", delta_color="inverse")
                st.progress(min(int(risk_probability), 100))
                
            st.markdown("""
            **Recommended Clinical Next Steps:**
            - **Cardiology Consultation:** Refer patient to a specialist for comprehensive cardiovascular workup.
            - **Further Diagnostic Testing:** Perform standard 12-lead ECG, Echocardiogram, or coronary CT angiography.
            - **Biomarker Management:** Monitor arterial pressure, lipid profile, and fasting blood glucose strictly.
            """)
        else:
            st.markdown(f"""
            <div class="result-box-low">
                <div class="result-title result-title-low">✅ Low Risk of Heart Disease Detected</div>
                <div class="result-desc">The predictive model indicates that patient parameters currently fall within low risk thresholds for cardiovascular complications.</div>
            </div>
            """, unsafe_allow_html=True)
            
            if risk_probability is not None:
                mcol1, mcol2 = st.columns(2)
                with mcol1:
                    st.metric("Estimated Risk Probability", f"{risk_probability:.1f}%")
                with mcol2:
                    st.metric("Risk Classification", "Low / Normal", delta="Healthy Range", delta_color="normal")
                st.progress(min(int(risk_probability), 100))
                
            st.markdown("""
            **Preventative Health Recommendations:**
            - **Regular Screening:** Schedule routine annual physical exams and cardiac health reviews.
            - **Active Lifestyle:** Maintain at least 150 minutes of moderate aerobic activity weekly.
            - **Balanced Diet:** Adopt a Mediterranean or DASH-style diet rich in fiber, whole grains, and lean proteins.
            """)

    with res_col2:
        st.markdown("#### 📋 Submitted Patient Profile")
        
        summary_data = {
            "Parameter": [
                "Age", "Sex", "Resting Blood Pressure", "Total Cholesterol", 
                "Fasting Blood Sugar", "Chest Pain Type", "Resting ECG", 
                "Max Heart Rate", "Exercise Angina", "Oldpeak (ST Depression)", "ST Slope"
            ],
            "Value": [
                f"{age} years",
                "Male" if sex == 'M' else "Female",
                f"{restingbp} mm Hg",
                f"{cholesterol} mg/dL",
                "> 120 mg/dL" if fasting_bs == 1 else "≤ 120 mg/dL",
                chest_pain_labels.get(chest_pain, chest_pain),
                ecg_labels.get(resting_ecg, resting_ecg),
                f"{max_hr} bpm",
                "Yes" if exercise_angina == 'Y' else "No",
                f"{oldpeak}",
                st_slope_labels.get(st_slope, st_slope)
            ]
        }
        st.dataframe(pd.DataFrame(summary_data), use_container_width=True, hide_index=True)
