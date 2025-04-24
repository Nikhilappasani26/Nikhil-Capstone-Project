# Nikhil-Capstone-Project
💳 Credit Default Prediction: A Machine Learning & Deep Learning Approach
🚨 Problem Statement
Credit default—when borrowers fail to repay loans—poses a serious risk to financial institutions. Traditional risk assessment relies heavily on manual review and basic scoring, which are:

Time-consuming

Inaccurate

Not scalable

This project aims to automate and optimize the credit risk prediction process using Random Forest and Neural Network models, leveraging customer financial and behavioral data.

🎯 Project Goals
This repository delivers a complete solution that includes:

End-to-end data analysis and modeling

Predictive classification using ML & DL

A Streamlit-powered dashboard for interactive credit risk prediction

Model explainability using SHAP values

🌍 Why This Project Matters
🏦 Financial Stability
Minimizing default risk is key to maintaining healthy loan portfolios.

⚙️ Innovation in FinTech
Automation with interpretable AI enables real-time and scalable credit scoring.

🚀 Operational Efficiency
AI-driven tools reduce reliance on human analysts and accelerate decision-making.

👥 Target Audience
🏛 Banks & Lending Institutions

💼 FinTech Companies

📊 Credit Risk Analysts

📜 Regulatory Authorities & Policy Makers

📁 Project Structure
mathematica
Copy
Edit
📦 Credit-Default-Prediction
 ┣ 📄 Nikhil_app.py               → Streamlit web app
 ┣ 📄 random_forest.pkl           → Trained Random Forest model
 ┣ 📄 credit_score_dataset.csv    → Dataset file
 ┗ 📄 README.md                   → Project documentation
📊 Dataset Overview
Source: Kaggle – Credit Score Dataset

Size: ~1000 customer records | 84 features

Important Features:

CREDIT_SCORE

DEFAULT (0 = No Default, 1 = Default)

Ratios: R_SAVINGS_INCOME, R_DEBT_INCOME, R_DEBT_SAVINGS

Expenditures: T_GROCERIES_6, T_HEALTH_12, etc.

Categorical flags: credit card ownership, mortgage, dependents

🔍 Key Insights from Data Exploration
Label Imbalance: Fewer defaulters than non-defaulters

Feature Skew: Right-skewed income, savings, and debt values

Behavioral Patterns: Spending on gambling/entertainment linked to default risk

Visuals Used: Histograms, swarm plots, violin plots, boxplots

🤖 Modeling Approach
1️⃣ Random Forest Classifier
Ensemble method with decision trees

Reduces overfitting and handles complex interactions

Trained using top features selected by SelectKBest

2️⃣ Fine-Tuned Neural Network
Architecture: 3 layers with 128, 64, 32 neurons

Optimized using:

Dropout

Batch Normalization

Early Stopping

Adam Optimizer (Binary Cross-Entropy Loss)

Achieved better generalization through learning rate tuning

📈 Train/Test Split: 80% train | 20% test

🏆 Model Performance

Model	Accuracy
Random Forest	71.5%
Neural Network	74.0%
Neural Network provided superior performance

Both models are strong but can improve with larger datasets

🔎 Explainable AI with SHAP
SHAP (SHapley Additive exPlanations) was used to:

Explain individual predictions

Highlight feature contributions

Enable transparency for stakeholders

🧠 Top Contributing Features:

CREDIT_SCORE

CAT_CREDIT_CARD

R_DEBT_INCOME

🖥 Streamlit Web Application
A user-friendly, interactive dashboard built using Streamlit allows stakeholders to:

✅ Input borrower data
✅ Get instant default risk prediction (High/Low)
✅ View feature impact using SHAP
✅ Make real-time loan decisions

🚀 How to Launch the App Locally
🗂 Place These Files in One Folder:
credit_score_dataset.csv

Nikhil_app.py

random_forest.pkl

🛠 Install dependencies (if not already):
bash
Copy
Edit
pip install streamlit pandas numpy scikit-learn shap
▶️ Run the app:
bash
Copy
Edit
streamlit run Nikhil_app.py
This will open a browser window where you can interact with the credit risk dashboard.
