import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("rf_income_model.pkl")

st.title("Income Prediction (Random Forest)")

# === Dictionaries to encode human-readable labels ===
workclass_options = ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov',
                     'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']
education_options = ['Bachelors', 'HS-grad', '11th', 'Masters', '9th', 'Some-college',
                     'Assoc-acdm', 'Assoc-voc', '7th-8th', 'Doctorate', 'Prof-school',
                     '5th-6th', '10th', '1st-4th', 'Preschool', '12th']
marital_status_options = ['Married-civ-spouse', 'Divorced', 'Never-married',
                          'Separated', 'Widowed', 'Married-spouse-absent']
occupation_options = ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial',
                      'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical',
                      'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']
relationship_options = ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']
race_options = ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
gender_options = ['Male', 'Female']
native_country_options = ['United-States', 'Mexico', 'Philippines', 'Germany', 'Canada', 'India', 'England',
                          'Puerto-Rico', 'Cuba', 'Jamaica', 'South', 'China', 'Italy', 'Poland', 'Columbia',
                          'Haiti', 'Japan', 'Iran', 'Greece', 'Portugal', 'Nicaragua', 'Vietnam', 'Ireland',
                          'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Honduras',
                          'Thailand', 'Hong', 'Hungary', 'Guatemala', 'Scotland', 'Trinadad&Tobago',
                          'Yugoslavia', 'Outlying-US(Guam-USVI-etc)', 'Peru', 'Holand-Netherlands']

# === User Inputs with readable dropdowns ===
age = st.number_input("Age", 17, 90)
workclass = st.selectbox("Workclass", workclass_options)
education = st.selectbox("Education", education_options)
marital_status = st.selectbox("Marital Status", marital_status_options)
occupation = st.selectbox("Occupation", occupation_options)
relationship = st.selectbox("Relationship", relationship_options)
race = st.selectbox("Race", race_options)
gender = st.radio("Gender", gender_options)
hours_per_week = st.slider("Hours per Week", 1, 99, 40)
native_country = st.selectbox("Native Country", native_country_options)

# === Convert to encoded values ===
input_data = {
    'age': age,
    'workclass': workclass_options.index(workclass),
    'fnlwgt': 100000,  # dummy
    'education': education_options.index(education),
    'educational-num': 10,  # dummy
    'marital-status': marital_status_options.index(marital_status),
    'occupation': occupation_options.index(occupation),
    'relationship': relationship_options.index(relationship),
    'race': race_options.index(race),
    'gender': gender_options.index(gender),
    'capital-gain': 0,       # dummy
    'capital-loss': 0,       # dummy
    'hours-per-week': hours_per_week,
    'native-country': native_country_options.index(native_country)
}

# Predict
input_df = pd.DataFrame([input_data])
if st.button("Predict Income"):
    prediction = model.predict(input_df)[0]
    label = ">50K" if prediction == 1 else "<=50K"
    st.success(f"Predicted Income: {label}")
