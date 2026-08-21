# 📊 Customer Churn Prediction

An end-to-end machine learning project for predicting customer churn using customer demographic, service, contract, and billing information.

The project covers exploratory data analysis, model comparison, feature importance analysis, threshold optimization, and deployment with Streamlit.

---

## 🎯 Project Overview

Customer churn is an important business problem for telecommunications companies.

The goal of this project is to predict whether a customer is likely to churn and identify customer characteristics associated with higher churn risk.

The final model provides:

* Churn probability
* Churn / No Churn prediction
* Risk classification through a customized decision threshold
* Interactive prediction through a Streamlit web application

---

## 📂 Dataset

The dataset contains **7,043 customer records** and information about:

* Customer demographics
* Internet and phone services
* Contract information
* Payment methods
* Monthly charges
* Total charges
* Customer tenure
* Churn status

### Target Variable

The target variable is:

```text
Churn Label
```

Where:

* `No` = Customer stays
* `Yes` = Customer churns

### Class Distribution

* **5,174** non-churned customers
* **1,869** churned customers
* **Churn rate: 26.54%**

---

## 🔎 Exploratory Data Analysis

Several customer characteristics were analyzed to understand their relationship with churn.

### Contract

Customers with month-to-month contracts showed substantially higher churn than customers with one-year or two-year contracts.

| Contract       | Churn Rate |
| -------------- | ---------: |
| Month-to-month |     42.71% |
| One year       |     11.27% |
| Two year       |      2.83% |

### Internet Service

Fiber optic customers showed a higher churn rate compared with DSL customers.

| Internet Service | Churn Rate |
| ---------------- | ---------: |
| DSL              |     18.96% |
| Fiber optic      |     41.89% |
| No Internet      |      7.40% |

### Payment Method

Electronic check customers had a notably higher churn rate.

| Payment Method   | Churn Rate |
| ---------------- | ---------: |
| Bank transfer    |     16.71% |
| Credit card      |     15.24% |
| Electronic check |     45.29% |
| Mailed check     |     19.11% |

### Technical Support

Customers without technical support had a substantially higher churn rate.

| Tech Support        | Churn Rate |
| ------------------- | ---------: |
| No                  |     41.64% |
| Yes                 |     15.17% |
| No internet service |      7.40% |

These patterns were used as part of the feature analysis and model interpretation.

---

## 🤖 Machine Learning

Three classification models were evaluated:

1. Logistic Regression
2. Random Forest
3. XGBoost

### Model Comparison

The XGBoost model achieved the highest ROC-AUC among the evaluated models.

| Model               |   ROC-AUC |
| ------------------- | --------: |
| Logistic Regression |     0.849 |
| Random Forest       |     0.834 |
| XGBoost             | **0.856** |

The final model was selected based on its overall predictive performance, particularly ROC-AUC.

---

## 📈 XGBoost Performance

Before threshold optimization, the XGBoost model achieved:

* **Accuracy:** 80.48%
* **ROC-AUC:** 0.856

### Classification Performance

| Class    | Precision | Recall | F1-score |
| -------- | --------: | -----: | -------: |
| No Churn |      0.85 |   0.89 |     0.87 |
| Churn    |      0.65 |   0.56 |     0.60 |

---

## 🎚️ Threshold Optimization

Because identifying customers who are likely to churn is important, the default classification threshold of **0.50** was evaluated.

A lower threshold was tested to improve recall for the churn class.

### Selected Threshold

The selected threshold was:

```text
0.35
```

At this threshold:

* **Churn Precision:** 0.50
* **Churn Recall:** 0.81
* **Churn F1-score:** 0.62

This increases the model's ability to identify potential churners, at the cost of lower overall accuracy.

### Why 0.35?

The threshold was selected to prioritize recall for the churn class.

In a business setting, missing a customer who is likely to churn may be more costly than contacting some customers who ultimately stay.

---

## ⭐ Feature Importance

The most important features identified by the final model included:

| Feature                          | Importance |
| -------------------------------- | ---------: |
| Total Charges                    |      0.135 |
| Tenure Months                    |      0.125 |
| Monthly Charges                  |      0.119 |
| Contract: Month-to-month         |      0.072 |
| Online Security: No              |      0.037 |
| Contract: Two year               |      0.034 |
| Tech Support: No                 |      0.031 |
| Dependents: Yes                  |      0.027 |
| Payment Method: Electronic check |      0.027 |
| Internet Service: Fiber optic    |      0.026 |

These features provide useful insight into factors associated with customer churn.

---

## 🌐 Streamlit Application

The trained model was deployed as an interactive Streamlit application.

Users can enter customer information such as:

* Gender
* Senior citizen status
* Partner and dependents
* Tenure
* Internet service
* Online security
* Technical support
* Contract type
* Payment method
* Monthly charges
* Total charges

The application returns:

* **Churn Probability**
* **Churn / No Churn Prediction**

### Example

```text
Churn Probability: 48.00%

⚠️ High Risk: Customer is likely to churn.
```

---

## 🛠️ Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Matplotlib
* Seaborn
* Jupyter Notebook
* Streamlit
* Git / GitHub

---

## 📁 Project Structure

```text
customer-churn-prediction/
│
├── data/
│
├── models/
│   ├── churn_model.pkl
│   └── threshold.pkl
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│   └── 02_model_training.ipynb
│
├── src/
│   └── predict.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

> Trained `.pkl` model files are excluded from Git tracking.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/arsu-maehae/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📌 Key Takeaways

This project demonstrates an end-to-end machine learning workflow:

```text
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Preparation
     ↓
Model Training
     ↓
Model Comparison
     ↓
Feature Importance
     ↓
Threshold Optimization
     ↓
Model Deployment
```

The project focuses not only on model accuracy, but also on business-oriented evaluation, particularly improving the ability to identify customers who are at risk of churn.

---

## 🔮 Future Improvements

Potential improvements include:

* Hyperparameter tuning
* Cross-validation
* Model calibration
* Explainable AI using SHAP
* Customer segmentation
* Automated model retraining
* Cloud deployment
* Monitoring model performance over time
