import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("credit_risk_model.pkl")

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(page_title="Credit Risk Prediction", layout="centered")

st.title("💳 Credit Risk Prediction System")
st.write("Enter borrower details to predict loan default risk")

# -----------------------------
# INPUT SECTION
# -----------------------------
age = st.number_input("Age", 18, 100, 25)
income = st.number_input("Income", 1000, 1000000, 50000)
emp_exp = st.number_input("Employment Experience (years)", 0, 40, 2)
loan_amnt = st.number_input("Loan Amount", 1000, 1000000, 10000)
interest = st.number_input("Interest Rate (%)", 0.0, 30.0, 12.5)
loan_percent_income = st.number_input("Loan % of Income", 0.0, 1.0, 0.2)
cred_hist = st.number_input("Credit History Length", 0, 30, 3)
credit_score = st.number_input("Credit Score", 300, 900, 650)

gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education", ["Bachelor", "Doctorate", "High School", "Master"])
home = st.selectbox("Home Ownership", ["OTHER", "OWN", "RENT"])
intent = st.selectbox("Loan Purpose", ["EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"])
prev_default = st.selectbox("Previous Loan Default", ["No", "Yes"])

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("Predict Risk"):

    # Encoding (same as training data)
    gender_male = 1 if gender == "Male" else 0

    edu_bach = 1 if education == "Bachelor" else 0
    edu_doc = 1 if education == "Doctorate" else 0
    edu_hs = 1 if education == "High School" else 0
    edu_master = 1 if education == "Master" else 0

    home_other = 1 if home == "OTHER" else 0
    home_own = 1 if home == "OWN" else 0
    home_rent = 1 if home == "RENT" else 0

    intent_edu = 1 if intent == "EDUCATION" else 0
    intent_home = 1 if intent == "HOMEIMPROVEMENT" else 0
    intent_med = 1 if intent == "MEDICAL" else 0
    intent_personal = 1 if intent == "PERSONAL" else 0
    intent_venture = 1 if intent == "VENTURE" else 0

    prev_def = 1 if prev_default == "Yes" else 0

    # Create input dataframe (MUST match training order)
    input_data = pd.DataFrame([[
        age, income, emp_exp, loan_amnt, interest,
        loan_percent_income, cred_hist, credit_score,
        gender_male,
        edu_bach, edu_doc, edu_hs, edu_master,
        home_other, home_own, home_rent,
        intent_edu, intent_home, intent_med,
        intent_personal, intent_venture,
        prev_def
    ]])

    # Prediction
    prob = model.predict_proba(input_data)[0][1]

    st.subheader("📊 Prediction Result")

    # Risk Levels
    if prob < 0.3:
        st.success(f"✅ Low Risk ({round(prob*100,2)}%)")
    elif prob < 0.7:
        st.warning(f"⚠️ Medium Risk ({round(prob*100,2)}%)")
    else:
        st.error(f"🚨 High Risk ({round(prob*100,2)}%)")

    st.write("Default Probability:", round(prob*100, 2), "%")
