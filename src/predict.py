import joblib


model = joblib.load("models/churn_model.pkl")
threshold = joblib.load("models/threshold.pkl")


def predict_churn(customer):
    probability = model.predict_proba(customer)[0, 1]

    prediction = int(probability >= threshold)

    return probability, prediction