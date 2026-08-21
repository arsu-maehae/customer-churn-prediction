import os
import joblib
import pandas as pd


# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "churn_model.pkl")
THRESHOLD_PATH = os.path.join(BASE_DIR, "models", "threshold.pkl")


# Load trained model and threshold
model = joblib.load(MODEL_PATH)
threshold = joblib.load(THRESHOLD_PATH)


def predict_churn(customer_data: pd.DataFrame):
    """
    Predict customer churn probability and class.

    Parameters
    ----------
    customer_data : pd.DataFrame
        Customer information with the same features used during training.

    Returns
    -------
    probability : float
        Probability of customer churn.
    prediction : int
        1 = Churn, 0 = No Churn.
    """

    probability = model.predict_proba(customer_data)[:, 1][0]

    prediction = int(probability >= threshold)

    return probability, prediction