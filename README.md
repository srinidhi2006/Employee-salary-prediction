# 💼 Income Prediction Web App (>$50K or <=$50K)

This project predicts whether an individual's annual income exceeds $50K using demographic and employment data. It uses a supervised machine learning model and is deployed using **Streamlit** for real-time web interaction.

---

## 🔍 Problem Statement

Human Resource departments often need to filter candidates based on potential income levels. This tool predicts whether a person earns more than $50K per year based on attributes like age, education, occupation, hours worked per week, etc.

---

## 🧠 Model Overview

- 
- **Algorithm Used**: Random Forest Classifier / XGBoost (initial version)
- **Preprocessing**:
  - Missing value handling (`?` → NaN → drop rows)
  - LabelEncoding or OneHotEncoding for categorical variables
- **Performance Note**:
  - The initial model was biased toward predicting income `<=50K` due to dataset imbalance
  - Future improvements aim to handle this with SMOTE or class weighting

---

## 🚀 Features

- 🔮 Predicts if income is `>50K` or `<=50K`
- 📊 User inputs via a friendly Streamlit web interface
- 💡 Deployed publicly for real-time use

---

## 🧱 Technologies Used

| Component        | Tech Stack                  |
|------------------|-----------------------------|
| ML Model         | scikit-learn (RandomForest) |
| Web Interface    | Streamlit                   |
| Data Handling    | pandas, joblib              |
| Deployment       | Streamlit Cloud             |

---

## 📂 Project Structure


├── app.py # Streamlit app
├── income_compressed_pipeline.pkl # Trained and compressed model
├── requirements.txt # Python dependencies
├── README.md # Project info (this file)

🌐 Deployed Version
🔗 Live Demo: https://employee-salary-prediction-vhh2rjpcsyq4qpsgkd2jed.streamlit.app/

Developed by T. Srinidhi
Bachelor of Technology, Computer Science (Data Science)
Vellore Institute of Technology, Chennai
