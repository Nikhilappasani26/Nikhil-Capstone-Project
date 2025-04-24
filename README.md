Credit Default Status Prediction Using Machine Learning and Deep Learning
What Problem Did I Try to Solve?
Credit default occurs when borrowers fail to repay loans, posing a significant threat to financial institutions. Traditional credit risk assessments are manual, slow, and often inaccurate.
The goal of this project was to automate and enhance the accuracy of credit risk predictions using machine learning (Random Forest) and deep learning (Neural Networks), trained on customer financial and demographic data.

This repository contains code, analysis, and an interactive Streamlit-based web dashboard for classifying borrowers as default or non-default using modern AI methods.

Why Is This Project Important?
Financial Stability: Misjudging credit risk can lead to high non-performing loans and financial collapse for institutions.
Technological Innovation: Automation with interpretable AI helps in real-time, high-accuracy risk prediction.
Operational Efficiency: Reduces the need for manual analysis and accelerates loan approval processes.

Who are the stakeholders or target audience?
Banks & Financial Institutions

FinTech Companies

Credit Risk Analysts

Policy Makers & Regulators

Table of Contents
Dataset

Exploratory Data Analysis

Modeling

Results

Explainability

Streamlit Dashboard

How to Run the App

Dataset
Source: Kaggle (https://www.kaggle.com/datasets/conorsully1/credit-score)
File: Credit Score Dataset
Size: ~1000 customer records with 84 features
Key Columns:

CREDIT_SCORE: Numeric representation of creditworthiness

DEFAULT: Target label (1 = Default, 0 = No Default)

Financial Ratios: R_SAVINGS_INCOME, R_DEBT_INCOME, R_DEBT_SAVINGS

Expenditures: T_GROCERIES_6, T_HEALTH_12, etc.

Categorical indicators: credit card, mortgage, dependents

Exploratory Data Analysis
Label Distribution: Imbalanced data with fewer defaults than non-defaults

Feature Distributions: Right-skewed distributions in income, debt, savings

Behavioral Traits: Gambling and entertainment spend show correlation with defaults

Visualizations: Histograms, violin plots, swarm plots, box plots, etc.

Modeling
Two main classifiers were trained:

Random Forest Classifier

Ensemble method using multiple decision trees

Helps reduce overfitting

Trained on selected best features (via SelectKBest)

Neural Network (Fine-Tuned)

Architecture: 3 hidden layers with 128, 64, and 32 neurons

Techniques: Dropout, Batch Normalization, Early Stopping

Loss: Binary cross-entropy, Optimizer: Adam

Lower learning rate and tuned architecture improved generalization

Split: 80% training, 20% testing

Results

Model	Accuracy
Random Forest	71.5%
Neural Network	74.0%
Neural Network outperformed the Random Forest in overall classification accuracy.

Both models showed reasonable precision and recall but can be improved with more data.

Explainability
SHAP (SHapley Additive exPlanations)

Feature importance analysis

Shows individual feature impact on predictions

Top Influencers: CREDIT_SCORE, CAT_CREDIT_CARD, R_DEBT_INCOME

Streamlit Dashboard
An interactive Streamlit-based dashboard has been developed for real-time credit risk evaluation.

Input Fields: Credit score, ratios (debt-to-income, savings-to-income), expenditure category weights, etc.

Predict Button: Classifies borrower as "High Risk" or "Low Risk"

Explainability: SHAP insights help understand what drove the prediction

Use Case: Ideal for financial institutions to assess loan applications interactively

How to Run the App
To use the app, ensure the following files are in the same folder:

credit_score_dataset.csv – the input data

Nikhil_app.py – the Streamlit app script

random_forest.pkl – the trained Random Forest model
