import streamlit as st
import pandas as pd
import joblib
import random

# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load("credit_risk_model.pkl")

st.set_page_config(page_title="Credit Risk Dashboard", layout="wide")

# -----------------------------
# CHATBOT LOGIC (SMART LOCAL)
# -----------------------------
def smart_chatbot(user_input):
    text = user_input.lower()

    responses = []

    if "risk" in text:
        responses.append("Risk is calculated using multiple financial factors like income, credit score, and loan burden.")

    if "credit score" in text:
        responses.append("A higher credit score reduces default risk. Scores above 700 are generally considered good.")

    if "loan" in text:
        responses.append("Loan amount and loan percentage of income are critical. Higher values increase risk.")

    if "income" in text:
        responses.append("Higher income generally lowers risk as repayment capacity improves.")

    if "default" in text:
        responses.append("Previous defaults significantly increase the probability of future default.")

    if "improve" in text or "reduce risk" in text:
        responses.append("To reduce risk, increase income, reduce loan burden, and maintain a good credit history.")

    if not responses:
        responses.append("I can help you understand credit risk, loan factors, and prediction results. Try asking about income, credit score, or default.")

    return random.choice(responses)

# -----------------------------
# SIDEBAR INPUT
# -----------------------------
st.sidebar.title("💳 Loan Input Panel")

age = st.sidebar.slider("Age", 18, 100, 25)
income = st.sidebar.number_input("Income", 1000, 1000000, 50000)
emp_exp = st.sidebar.slider("Experience", 0, 40, 2)
loan_amnt = st.sidebar.number_input("Loan Amount", 1000, 1000000, 10000)
interest = st.sidebar.slider("Interest Rate", 0.0, 30.0, 12.5)

loan_percent_income = st.sidebar.slider("Loan % Income", 0.0, 1.0, 0.2)
cred_hist = st.sidebar.slider("Credit History", 0, 30, 3)
credit_score = st.sidebar.slider("Credit Score", 300, 900, 650)

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
education = st.sidebar.selectbox("Education", ["Bachelor", "Doctorate", "High School", "Master"])
home = st.sidebar.selectbox("Home Ownership", ["OTHER", "OWN", "RENT"])
intent = st.sidebar.selectbox("Loan Purpose", ["EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"])
prev_default = st.sidebar.selectbox("Previous Default", ["No", "Yes"])

# -----------------------------
# MAIN TITLE
# -----------------------------
st.title("📊 Credit Risk Analytics Dashboard")

# -----------------------------
# ENCODING
# -----------------------------
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

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("🚀 Analyze Risk"):

    prob = model.predict_proba(input_data)[0][1]

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Income", income)
    col2.metric("📈 Credit Score", credit_score)
    col3.metric("📊 Loan %", loan_percent_income)

    st.divider()

    st.subheader("📊 Risk Result")

    if prob < 0.3:
        st.success(f"🟢 Low Risk ({round(prob*100,2)}%)")
    elif prob < 0.7:
        st.warning(f"🟡 Medium Risk ({round(prob*100,2)}%)")
    else:
        st.error(f"🔴 High Risk ({round(prob*100,2)}%)")

    st.progress(prob)

    st.subheader("📌 Insights")

    if credit_score < 600:
        st.write("⚠️ Low credit score increases risk")
    if loan_percent_income > 0.4:
        st.write("⚠️ High loan burden detected")
    if prev_def == 1:
        st.write("🚨 Previous default increases risk")

# -----------------------------
# CHATBOT SECTION
# -----------------------------
st.sidebar.markdown("## 🤖 AI Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_msg = st.sidebar.text_input("Ask about credit risk:")

if st.sidebar.button("Send"):
    if user_msg:
        reply = smart_chatbot(user_msg)
        st.session_state.chat_history.append(("You", user_msg))
        st.session_state.chat_history.append(("Bot", reply))

for role, msg in st.session_state.chat_history:
    if role == "You":
        st.sidebar.markdown(f"🧑 {msg}")
    else:
        st.sidebar.markdown(f"🤖 {msg}")
