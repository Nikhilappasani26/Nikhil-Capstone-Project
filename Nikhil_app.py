import streamlit as st
import pickle
import pandas as pd

# Load model
@st.cache_resource
def load_model():
    with open("random_forest.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# Streamlit UI
st.title("Credit Default Prediction Dashboard")
st.write("Enter borrower details to predict default risk.")

# Input fields
R_DEBT_INCOME = st.number_input("Debt-to-Income Ratio", 0.0, 1.0, step=0.01)
R_DEBT_SAVINGS = st.number_input("Debt-to-Savings Ratio", 0.0, 1.0, step=0.01)
R_ENTERTAINMENT_DEBT = st.number_input("Entertainment Debt", 0.0, 1.0, step=0.01)
R_GROCERIES_DEBT = st.number_input("Groceries Debt", 0.0, 1.0, step=0.01)
R_HEALTH_DEBT = st.number_input("Health Debt", 0.0, 1.0, step=0.01)
R_TAX_DEBT = st.number_input("Tax Debt", 0.0, 1.0, step=0.01)
R_UTILITIES_DEBT = st.number_input("Utilities Debt", 0.0, 1.0, step=0.01)
R_EXPENDITURE_DEBT = st.number_input("Expenditure Debt", 0.0, 1.0, step=0.01)
CAT_CREDIT_CARD = st.selectbox("Has Credit Card?", [0, 1])
CREDIT_SCORE = st.number_input("Credit Score", 300, 850)

# Predict button
if st.button("Predict Default Risk"):
    input_data = pd.DataFrame([[R_DEBT_INCOME, R_DEBT_SAVINGS, R_ENTERTAINMENT_DEBT, 
                                R_GROCERIES_DEBT, R_HEALTH_DEBT, R_TAX_DEBT, R_UTILITIES_DEBT,
                                R_EXPENDITURE_DEBT, CAT_CREDIT_CARD, CREDIT_SCORE]],
                              columns=['R_DEBT_INCOME', 'R_DEBT_SAVINGS', 'R_ENTERTAINMENT_DEBT',
                                       'R_GROCERIES_DEBT', 'R_HEALTH_DEBT', 'R_TAX_DEBT', 'R_UTILITIES_DEBT',
                                       'R_EXPENDITURE_DEBT', 'CAT_CREDIT_CARD', 'CREDIT_SCORE'])

    prediction = model.predict(input_data)[0]
    st.write(f"### **Predicted Default Risk: {'High' if prediction == 1 else 'Low'}**")

