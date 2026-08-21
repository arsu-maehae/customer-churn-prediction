import streamlit as st
import pandas as pd

from src.predict import predict_churn


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)


st.title("📊 Customer Churn Prediction")
st.write(
    "Predict whether a customer is likely to churn "
    "based on their service and account information."
)


st.divider()


# Customer information
st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    tenure_months = st.number_input(
        "Tenure Months",
        min_value=0,
        max_value=100,
        value=12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )


with col2:
    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )


payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)


monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0,
    step=1.0
)


total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=840.0,
    step=10.0
)


st.divider()


# Prediction
if st.button(
    "🔮 Predict Churn",
    use_container_width=True
):

    customer_data = pd.DataFrame({
        "Gender": [gender],
        "Senior Citizen": [senior_citizen],
        "Partner": [partner],
        "Dependents": [dependents],
        "Tenure Months": [tenure_months],
        "Phone Service": [phone_service],
        "Multiple Lines": [multiple_lines],
        "Internet Service": [internet_service],
        "Online Security": [online_security],
        "Online Backup": [online_backup],
        "Device Protection": [device_protection],
        "Tech Support": [tech_support],
        "Streaming TV": [streaming_tv],
        "Streaming Movies": [streaming_movies],
        "Contract": [contract],
        "Paperless Billing": [paperless_billing],
        "Payment Method": [payment_method],
        "Monthly Charges": [monthly_charges],
        "Total Charges": [total_charges]
    })

    probability, prediction = predict_churn(customer_data)

    probability_percent = probability * 100

    st.subheader("Prediction Result")

    st.metric(
        "Churn Probability",
        f"{probability_percent:.2f}%"
    )

    if prediction == 1:
        st.error(
            "⚠️ High Risk: Customer is likely to churn."
        )
    else:
        st.success(
            "✅ Low Risk: Customer is unlikely to churn."
        )