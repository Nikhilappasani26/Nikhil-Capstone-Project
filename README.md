# 💳 Credit Default Prediction  
### 🔍 Machine Learning & Deep Learning for Financial Risk Forecasting  

---

## 🧠 What Problem Did I Try to Solve?

> **Credit default** — when borrowers fail to repay — is a **critical challenge** for financial institutions.  
> Traditional credit risk systems are **manual, error-prone, and slow**.  

🎯 **Goal**: Use **ML & DL models** to build a **predictive system** that automates and improves the accuracy of loan default prediction — using customer financial, demographic, and behavioral data.

This repo includes:
- 📊 Data Analysis
- 🤖 ML & DL Model Training
- 🖥️ Streamlit Dashboard
- 🧠 SHAP-based Explainable AI

---

## 🚀 Why This Project Matters

### 🏦 Financial Impact  
Helps reduce **non-performing loans** and boosts financial stability.

### 🧠 Smart Automation  
Real-time predictions with **explainable AI** models.

### 📈 Industry Use Case  
Streamlines loan assessments for banks, lenders, and credit platforms.

---

## 👥 Who Will Benefit?

- 🏛 **Banks & Lending Institutions**  
- 💼 **FinTech Startups**  
- 📊 **Credit Risk Analysts**  
- 📜 **Policy Makers & Financial Auditors**

---

## 🧾 Table of Contents

- [📁 Dataset](#-dataset)
- [📊 Exploratory Data Analysis](#-exploratory-data-analysis)
- [⚙️ Modeling](#️-modeling)
- [📉 Results](#-results)
- [🧠 Explainability](#-explainability)
- [🖥️ Streamlit Dashboard](#️-streamlit-dashboard)
- [🛠 How to Run the App](#-how-to-run-the-app)
- [📜 License](#-license)

---

## 📁 Dataset

- **Source**: [Kaggle – Credit Score Dataset](https://www.kaggle.com/datasets/conorsully1/credit-score)  
- **Size**: ~1000 records, 84 features  
- **Key Fields**:
  - `CREDIT_SCORE` – Numeric score  
  - `DEFAULT` – Target label (1 = Default, 0 = No Default)  
  - Financial Ratios: `R_SAVINGS_INCOME`, `R_DEBT_INCOME`, `R_DEBT_SAVINGS`  
  - Spending: `T_GROCERIES_6`, `T_HEALTH_12`  
  - Flags: Credit card, mortgage, dependents

---

## 📊 Exploratory Data Analysis

### 📌 Key Insights:
- 🔺 **Imbalanced** classes: fewer defaults  
- 📉 **Right-skewed** data in income, savings, debt  
- 🧩 Behavior links: gambling & entertainment → high default probability

### 📈 Visuals Used:
- 📊 Histograms  
- 🐝 Swarm plots  
- 🎻 Violin plots  
- 📦 Box plots  

---

## ⚙️ Modeling

### 1️⃣ **Random Forest Classifier**
- ✅ Ensemble of decision trees  
- ✅ Reduced overfitting  
- ✅ Features selected using `SelectKBest`

### 2️⃣ **Fine-Tuned Neural Network**
- 🔗 Layers: 128 → 64 → 32 neurons  
- 🧱 Batch Normalization, Dropout  
- 🧠 Loss: Binary Cross-Entropy | Optimizer: Adam  
- ⏱ Early Stopping | 🔧 Learning Rate Tuned  

📌 **Data Split**: 80% Train / 20% Test

---

## 📉 Results

| 🧪 Model            | 🎯 Accuracy |
|---------------------|-------------|
| ✅ Random Forest     | 71.5%        |
| 🚀 Neural Network    | **74.0%**    |

> 🧠 Neural Network outperformed Random Forest  
> 📉 Metrics: Precision, Recall, F1 Score evaluated for both

---

## 🧠 Explainability

### 🔍 SHAP (SHapley Additive exPlanations)
- 🎯 Local & global feature impact  
- 📊 Visual interpretation of how each feature affects the outcome

### 🌟 Top Influencing Features:
- `CREDIT_SCORE`  
- `CAT_CREDIT_CARD`  
- `R_DEBT_INCOME`  
- `R_DEBT_SAVINGS`

---

## 🖥️ Streamlit Dashboard

An interactive **web-based tool** built with `Streamlit` to:

✅ Input borrower info  
✅ Predict default risk in real-time  
✅ Visualize feature impact using **SHAP**  

> Ideal for **financial professionals** making live lending decisions.

---

## 🛠 How to Run the App

### 📂 Folder Structure:
