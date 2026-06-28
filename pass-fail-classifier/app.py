import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# =========================
# LOAD MODEL
# =========================
model_path = os.path.join(os.path.dirname(__file__), "model", "pass_fail_model.pkl")
model = joblib.load(model_path)
# =========================
# HEADER (PROFESSIONAL STYLE)
# =========================
st.markdown("""
# 🎓 AI Student Performance Predictor
### Predict student success using Machine Learning
---
""")

# =========================
# SIDEBAR (CLEAN CONTROL PANEL)
# =========================
st.sidebar.header("📊 Input Student Data")

math = st.sidebar.slider("Math Score", 0, 100, 50)
reading = st.sidebar.slider("Reading Score", 0, 100, 50)
writing = st.sidebar.slider("Writing Score", 0, 100, 50)

st.sidebar.markdown("---")
st.sidebar.info("This AI model predicts PASS or FAIL based on academic performance.")

# =========================
# MAIN LAYOUT (CLEAN DASHBOARD)
# =========================
col1, col2 = st.columns([2, 1])

# -------------------------
# LEFT SIDE - INPUT SUMMARY
# -------------------------
with col1:
    st.subheader("📘 Student Performance Overview")

    data_chart = pd.DataFrame({
        "Subject": ["Math", "Reading", "Writing"],
        "Score": [math, reading, writing]
    })

    st.bar_chart(data_chart.set_index("Subject"))

    st.markdown("### 📌 Input Summary")
    st.write(f"Math Score: **{math}**")
    st.write(f"Reading Score: **{reading}**")
    st.write(f"Writing Score: **{writing}**")

# -------------------------
# RIGHT SIDE - PREDICTION PANEL
# -------------------------
with col2:
    st.subheader("🤖 AI Prediction Panel")

    # Load dataset for feature structure
    df = pd.read_csv("data/StudentsPerformance.csv")
    df_encoded = pd.get_dummies(df, drop_first=True)

    drop_cols = [col for col in ["math score", "pass"] if col in df_encoded.columns]
    feature_columns = df_encoded.drop(drop_cols, axis=1).columns

    input_data = pd.DataFrame(np.zeros((1, len(feature_columns))), columns=feature_columns)

    if "math score" in input_data.columns:
        input_data["math score"] = math
    if "reading score" in input_data.columns:
        input_data["reading score"] = reading
    if "writing score" in input_data.columns:
        input_data["writing score"] = writing

    # Predict button
    if st.button("🚀 Predict Result"):
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.success("🎉 PASS")
        else:
            st.error("❌ FAIL")

        # Probability
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(input_data)[0][1]
            st.metric("📊 Pass Probability", f"{prob:.2%}")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("💼 Built by Rehana Hassan | Machine Learning Project")