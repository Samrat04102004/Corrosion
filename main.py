import streamlit as st
import numpy as np
import joblib

# --- Load model and preprocessors ---
model = joblib.load('lgbm_pitting_model.pkl')
scaler = joblib.load('scaler.pkl')


# --- Define the feature order ---
feature_names = [
    'Al', 'Cr', 'Fe', 'pH', 'test temp(degree celcius)', 'Ni', 'M[cl-]', 'N', 'Mn', 'Mo', 'C', 'Si'
]

st.set_page_config(page_title="Pitting Potential Predictor", layout="centered")
st.title("Data-Driven Pitting Corrosion Prediction")
st.markdown("""
Enter alloy composition and test conditions to estimate pitting potential (mV SCE).  
This tool is designed for metallurgical engineers and corrosion scientists.
""")

with st.form("input_form"):
    st.subheader("Alloy Composition (wt.%)")
    Al = st.number_input("Al", min_value=0.0, max_value=100.0, value=0.0, step=0.01)
    Cr = st.number_input("Cr", min_value=0.0, max_value=100.0, value=18.0, step=0.01)
    Fe = st.number_input("Fe", min_value=0.0, max_value=100.0, value=60.0, step=0.01)
    Ni = st.number_input("Ni", min_value=0.0, max_value=100.0, value=10.0, step=0.01)
    Mo = st.number_input("Mo", min_value=0.0, max_value=100.0, value=2.0, step=0.01)
    N = st.number_input("N", min_value=0.0, max_value=100.0, value=0.0, step=0.001)
    Mn = st.number_input("Mn", min_value=0.0, max_value=100.0, value=1.0, step=0.01)
    C = st.number_input("C", min_value=0.0, max_value=100.0, value=0.03, step=0.001)
    Si = st.number_input("Si", min_value=0.0, max_value=100.0, value=1.0, step=0.01)

    st.subheader("Test Environment")
    pH = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0, step=0.01)
    temp = st.number_input("Test Temperature (°C)", min_value=0.0, max_value=120.0, value=25.0, step=0.1)
    cl = st.number_input("Chloride Concentration (M)", min_value=0.0, max_value=6.0, value=0.5, step=0.001)

    submitted = st.form_submit_button("Predict Pitting Potential")

if submitted:
    # Arrange input in the correct order
    input_data = np.array([[Al, Cr, Fe, pH, temp, Ni, cl, N, Mn, Mo, C, Si]])
    # Impute and scale
    input_data = scaler.transform(input_data)
    # Predict
    pred = model.predict(input_data)[0]

    # Risk assessment logic
    if pred < 0:
        risk_msg = "<b>Very High Risk:</b> Material is highly susceptible to pitting corrosion under these conditions."
        color = "#d32f2f"
    elif pred < 300:
        risk_msg = "<b>High Risk:</b> Significant likelihood of pitting corrosion; not recommended for aggressive environments."
        color = "#f57c00"
    elif pred < 600:
        risk_msg = "<b>Moderate Risk:</b> Some resistance, but pitting may occur in harsh or variable service."
        color = "#fbc02d"
    elif pred < 900:
        risk_msg = "<b>Low Risk:</b> Good resistance; suitable for most environments but monitor for severe exposures."
        color = "#388e3c"
    else:
        risk_msg = "<b>Very Low Risk:</b> Excellent pitting resistance; material is suitable for demanding applications."
        color = "#1976d2"

    st.markdown(f"### Predicted Pitting Potential: <span style='color:#1976d2'>{pred:.1f} mV SCE</span>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='padding:0.5em 1em;background:{color};color:white;border-radius:8px;font-size:1.1em;margin-top:1em'>{risk_msg}</div>",
        unsafe_allow_html=True
    )

    st.markdown("""
    ---
    <small>
    <b>Note:</b> This prediction is based on a machine learning model trained on published corrosion data.<br>
    """, unsafe_allow_html=True)


