import streamlit as st
import pandas as pd
from src.predict import predict_churn


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📊 Customer Churn Prediction")
st.write(
    "Predict whether a customer is likely to churn "
    "based on their service and account information."
)

st.divider()


# --------------------------------------------------
# Customer Information
# --------------------------------------------------

st.subheader("👤 Customer Information")

col1, col2, col3, col4 = st.columns(4)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

with col2:
    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

with col3:
    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

with col4:
    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )


col1, col2, col3 = st.columns(3)

with col1:
    tenure = st.number_input(
        "Tenure Months",
        min_value=0,
        max_value=72,
        value=12
    )

with col2:
    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

with col3:
    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=monthly_charges * tenure
    )


st.markdown("### 📡 Services")

col1, col2, col3, col4 = st.columns(4)

with col1:
    phone_service = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

with col2:
    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

with col3:
    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

with col4:
    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )


col1, col2, col3, col4 = st.columns(4)

with col1:
    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

with col2:
    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

with col3:
    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

with col4:
    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )


col1, col2 = st.columns(2)

with col1:
    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )

with col2:
    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )


st.markdown("### 💳 Billing")

col1, col2 = st.columns(2)

with col1:
    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

with col2:
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


st.divider()


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button(
    "🔮 Predict Churn Risk",
    use_container_width=True
):

    customer = pd.DataFrame([{
        "Gender": gender,
        "Senior Citizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "Tenure Months": tenure,
        "Phone Service": phone_service,
        "Multiple Lines": multiple_lines,
        "Internet Service": internet_service,
        "Online Security": online_security,
        "Online Backup": online_backup,
        "Device Protection": device_protection,
        "Tech Support": tech_support,
        "Streaming TV": streaming_tv,
        "Streaming Movies": streaming_movies,
        "Contract": contract,
        "Paperless Billing": paperless_billing,
        "Payment Method": payment_method,
        "Monthly Charges": monthly_charges,
        "Total Charges": total_charges
    }])

    probability, prediction = predict_churn(customer)

    st.divider()

    st.subheader("📈 Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Churn Probability",
            f"{probability:.2%}"
        )

    with col2:
        if prediction == 1:
            st.metric(
                "Prediction",
                "Churn"
            )
        else:
            st.metric(
                "Prediction",
                "No Churn"
            )

    st.progress(float(probability))

    if prediction == 1:
        st.error(
            "⚠️ High Risk: Customer is likely to churn."
        )
    else:
        st.success(
            "✅ Low Risk: Customer is unlikely to churn."
        )