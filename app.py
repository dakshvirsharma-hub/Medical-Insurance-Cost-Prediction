import streamlit as st
import pandas as pd
import joblib
# ------------------ Load Model ------------------ #
model = joblib.load("insurance.pkl")

# ------------------ Page Config ------------------ #
st.set_page_config(
    page_title="Insurance Charges Predictor",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Insurance Charges Prediction")
st.write("Fill in the details below and click **Predict**.")

# ------------------ User Inputs ------------------ #

age = st.slider(
    "Age",
    min_value=18,
    max_value=100,
    value=25
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0,
    step=0.1
)

children = st.slider(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

smoker = st.selectbox(
    "Smoker",
    ["No", "Yes"]
)

region = st.selectbox(
    "Region",
    [
        "Northeast",
        "Northwest",
        "Southeast",
        "Southwest"
    ]
)

# ------------------ Feature Engineering ------------------ #

# Gender
is_female = 1 if gender == "Female" else 0

# Smoker
is_smoker = 1 if smoker == "Yes" else 0

# Region Encoding
region_southeast = 1 if region == "Southeast" else 0
region_northwest = 1 if region == "Northwest" else 0

# BMI Category (Automatically generated)
bmi_category_Obese = 1 if bmi >= 30 else 0

# ------------------ Prediction ------------------ #

if st.button("Predict Insurance Charges"):

    input_df = pd.DataFrame({
        "age": [age],
        "is_female": [is_female],
        "bmi": [bmi],
        "children": [children],
        "is_smoker": [is_smoker],
        "region_southeast": [region_southeast],
        "bmi_category_Obese": [bmi_category_Obese],
        "region_northwest": [region_northwest]
    })

    prediction = model.predict(input_df)[0]

    st.success(f"💰 Estimated Insurance Charges: ₹ {prediction:,.2f}")

