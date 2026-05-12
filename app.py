import streamlit as st
import pandas as pd
import joblib
import random

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="PRISM - Credit Risk Dashboard",
    layout="wide"
)

# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load("credit_risk_model.pkl")

# =====================================================
# SMART CHATBOT FUNCTION
# =====================================================

def smart_chatbot(user_input):

    text = user_input.lower()
    responses = []

    if "risk" in text:
        responses.append(
            "Risk depends on income, credit score, loan burden, and previous defaults."
        )

    if "credit score" in text:
        responses.append(
            "Higher credit score means better repayment behavior and lower risk."
        )

    if "income" in text:
        responses.append(
            "Higher income improves repayment capacity and reduces risk."
        )

    if "loan" in text:
        responses.append(
            "Higher loan amount relative to income increases risk."
        )

    if "default" in text:
        responses.append(
            "Previous defaults strongly increase future risk."
        )

    if "reduce risk" in text or "improve" in text:
        responses.append(
            "Improve credit score, reduce loan burden, and maintain stable income."
        )

    if not responses:
        responses.append(
            "Ask me about risk, credit score, income, or loan factors."
        )

    return random.choice(responses)

# =====================================================
# SIDEBAR INPUTS
# =====================================================

st.sidebar.title("💳 Loan Input Panel")

age = st.sidebar.slider(
    "Age",
    18,
    100,
    25
)

income = st.sidebar.number_input(
    "Income",
    1000,
    1000000,
    50000
)

emp_exp = st.sidebar.slider(
    "Experience",
    0,
    40,
    2
)

loan_amnt = st.sidebar.number_input(
    "Loan Amount",
    1000,
    1000000,
    10000
)

interest = st.sidebar.slider(
    "Interest Rate",
    0.0,
    30.0,
    12.5
)

loan_percent_income = st.sidebar.slider(
    "Loan % Income",
    0.0,
    1.0,
    0.2
)

cred_hist = st.sidebar.slider(
    "Credit History",
    0,
    30,
    3
)

credit_score = st.sidebar.slider(
    "Credit Score",
    300,
    900,
    650
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

education = st.sidebar.selectbox(
    "Education",
    ["Bachelor", "Doctorate", "High School", "Master"]
)

home = st.sidebar.selectbox(
    "Home Ownership",
    ["OTHER", "OWN", "RENT"]
)

intent = st.sidebar.selectbox(
    "Loan Purpose",
    [
        "EDUCATION",
        "HOMEIMPROVEMENT",
        "MEDICAL",
        "PERSONAL",
        "VENTURE"
    ]
)

prev_default = st.sidebar.selectbox(
    "Previous Default",
    ["No", "Yes"]
)

# =====================================================
# MAIN + CHAT LAYOUT
# =====================================================

col_main, col_chat = st.columns([4, 1])

# =====================================================
# MAIN DASHBOARD
# =====================================================

with col_main:

    st.title("📊 PRISM - Credit Risk Analytics Dashboard")

    # =====================================================
    # ENCODING
    # =====================================================

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

    # =====================================================
    # INPUT DATAFRAME
    # =====================================================

    input_data = pd.DataFrame([[
        age,
        income,
        emp_exp,
        loan_amnt,
        interest,
        loan_percent_income,
        cred_hist,
        credit_score,
        gender_male,
        edu_bach,
        edu_doc,
        edu_hs,
        edu_master,
        home_other,
        home_own,
        home_rent,
        intent_edu,
        intent_home,
        intent_med,
        intent_personal,
        intent_venture,
        prev_def
    ]])

    # =====================================================
    # ANALYZE BUTTON
    # =====================================================

    if st.button("🚀 Analyze Risk"):

        prob = model.predict_proba(input_data)[0][1]

        # =====================================================
        # TOP METRICS
        # =====================================================

        col1, col2, col3 = st.columns(3)

        col1.metric("💰 Income", income)
        col2.metric("📈 Credit Score", credit_score)
        col3.metric("📊 Loan %", loan_percent_income)

        st.divider()

        # =====================================================
        # RISK RESULT
        # =====================================================

        st.subheader("📊 Risk Result")

        if prob < 0.3:

            st.success(
                f"🟢 Low Risk ({round(prob * 100, 2)}%)"
            )

        elif prob < 0.7:

            st.warning(
                f"🟡 Medium Risk ({round(prob * 100, 2)}%)"
            )

        else:

            st.error(
                f"🔴 High Risk ({round(prob * 100, 2)}%)"
            )

        # =====================================================
        # RISK PROGRESS BAR
        # =====================================================

        st.progress(prob)

        # =====================================================
        # INSIGHTS
        # =====================================================

        st.subheader("📌 Insights")

        if credit_score < 600:
            st.write("⚠️ Low credit score increases risk")

        if loan_percent_income > 0.4:
            st.write("⚠️ High loan burden detected")

        if prev_def == 1:
            st.write("🚨 Previous default increases risk")

        if income < 30000:
            st.write("💰 Lower income may affect repayment ability")

        if (
            credit_score >= 600
            and loan_percent_income <= 0.4
            and prev_def == 0
        ):
            st.success(
                "✅ Customer profile appears financially stable"
            )

        # =====================================================
        # VISUAL ANALYTICS
        # =====================================================

        st.subheader("📊 Visual Risk Analytics")

        chart1, chart2 = st.columns(2)

        # =====================================================
        # BAR CHART
        # =====================================================

        with chart1:

            st.markdown("### 📈 Risk Factors")

            bar_data = pd.DataFrame({
                "Factor": [
                    "Income",
                    "Credit Score",
                    "Loan %",
                    "Interest"
                ],

                "Value": [
                    income / 1000,
                    credit_score / 10,
                    loan_percent_income * 100,
                    interest * 10
                ]
            })

            st.bar_chart(
                bar_data.set_index("Factor")
            )

        # =====================================================
        # LINE CHART
        # =====================================================

        with chart2:

            st.markdown("### 📉 Financial Trend")

            line_data = pd.DataFrame({
                "Stage": [
                    "Experience",
                    "Credit History",
                    "Credit Score",
                    "Loan Burden"
                ],

                "Value": [
                    emp_exp * 10,
                    cred_hist * 10,
                    credit_score / 10,
                    loan_percent_income * 100
                ]
            })

            st.line_chart(
                line_data.set_index("Stage")
            )

        # =====================================================
        # AREA CHART
        # =====================================================

        st.markdown("### 📊 Risk Distribution")

        area_data = pd.DataFrame({
            "Safe": [100 - (prob * 100)],
            "Risk": [prob * 100]
        })

        st.area_chart(area_data)

        # =====================================================
        # OVERALL RISK METER
        # =====================================================

        st.subheader("🎯 Overall Risk Meter")

        st.progress(prob)

        st.write(
            f"### Risk Probability : {round(prob * 100, 2)}%"
        )

# =====================================================
# CHATBOT PANEL
# =====================================================

with col_chat:

    st.markdown("### 🤖 AI Assistant")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_msg = st.text_input("Ask something")

    if st.button("Send"):

        if user_msg:

            reply = smart_chatbot(user_msg)

            st.session_state.chat_history.append(
                ("You", user_msg)
            )

            st.session_state.chat_history.append(
                ("Bot", reply)
            )

    # =====================================================
    # DISPLAY CHAT
    # =====================================================

    for role, msg in st.session_state.chat_history:

        if role == "You":
            st.markdown(f"🧑 {msg}")

        else:
            st.markdown(f"🤖 {msg}")
