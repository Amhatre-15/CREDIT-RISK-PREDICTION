# 💳 Credit Risk Prediction System

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge\&logo=python\&logoColor=ffdd54)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Model-blue?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge\&logo=streamlit)
![Status](https://img.shields.io/badge/PROJECT-ONGOING-yellow?style=for-the-badge)

---

# 📌 Project Overview

This project builds a **Credit Risk Prediction System** using Machine Learning to determine whether a loan applicant is likely to be **safe or risky** for lending.

Financial institutions need to evaluate loan applications carefully to minimize the risk of default. This project demonstrates how **data science and machine learning models can help automate credit risk assessment**.

The project includes:

• Data analysis using **Python and Jupyter Notebook**
• Training a **machine learning classification model**
• Saving the trained model using **Pickle**
• Creating a **Streamlit web application** for user interaction

---

# 📂 Project Structure

```
credit-risk-prediction
│
├── Credit Risk Analysis.ipynb   # Data analysis and model training
├── LoansDataset.csv             # Dataset used for training
├── credit_risk_model.pkl        # Trained machine learning model
├── app.py                       # Streamlit web application
├── requirements.txt             # Required Python libraries
└── README.md                    # Project documentation
```

---

# ⚙️ Technologies Used

**Programming Language**

• Python

**Libraries & Tools**

• Pandas
• NumPy
• Scikit-learn
• Streamlit
• Pickle

---

# 🧠 Machine Learning Workflow

The project follows a typical **machine learning pipeline**:

### 1️⃣ Data Collection

A loan dataset containing borrower details such as:

* Age
* Income
* Loan amount
* Credit history
* Other financial indicators

---

### 2️⃣ Data Preprocessing

The dataset is cleaned and prepared by:

• Handling missing values
• Converting categorical variables
• Feature selection

---

### 3️⃣ Model Training

A machine learning classification model is trained to predict whether a loan is:

* **Safe**
* **Moderate Risk**
* **High Risk**

---

### 4️⃣ Model Saving

The trained model is saved using **Pickle** as:

```
credit_risk_model.pkl
```

This allows the model to be reused in the application without retraining.

---

### 5️⃣ Web Application

A **Streamlit app** (`app.py`) is built to allow users to input borrower details and receive a **risk prediction instantly**.

The app provides an interactive interface where users can enter:

• Age
• Income
• Loan information

The system then predicts the **credit risk category**.

---

# 🚀 How to Run the Project

### Step 1: Clone the repository

```
git clone https://github.com/Amhatre-15/credit-risk-prediction.git
```

---

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

---

### Step 3: Run the Streamlit application

```
streamlit run app.py
```

---

# 📊 Learning Outcomes

Built a machine learning model for credit risk classification.  
Performed data preprocessing and analysis.  
Saved the trained model using Pickle.  
Developed an interactive application using Streamlit.  
Published the project on GitHub.

---

# 🔮 Future Improvements

Use larger financial datasets.  
Test multiple machine learning models.  
Deploy the application online.  
Add advanced credit scoring features.

# Members
Atharva Mhatre
Niharika Pandey
Laxi Patel
Shubh Patel
Dhruv Patel
