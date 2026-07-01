# 🏥 Medical Insurance Cost Prediction

A Machine Learning project that predicts an individual's medical insurance charges based on personal and health-related information.

**Project Overview**

This project uses a **Gradient Boosting Regressor** trained on the Medical Insurance dataset to predict insurance charges based on demographic and lifestyle features. Multiple regression algorithms were trained and evaluated using **R² Score** and **Adjusted R²**. Gradient Boosting achieved the highest performance and was selected as the final model.

**Features Used**

- Age
- BMI
- Number of Children
- Smoker Status
- Gender
- Region

**Technologies Used**

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

**Models Performance**

| Model | R² Score | Adjusted R² | Status |
| :-------------------------------- | :------: | :---------: | :----------------: |
| **Gradient Boosting Regressor** | **0.90** | **0.90** | ⭐ Final Model |
| Random Forest Regressor | 0.89 | 0.89 | Tested |
| XGBoost Regressor | 0.89 | 0.89 | Tested |
| K-Nearest Neighbors Regressor | 0.84 | 0.84 | Tested |
| Decision Tree Regressor | 0.82 | 0.82 | Tested |
| Linear Regression | 0.75 | 0.75 | Tested |
| Ridge Regression | 0.75 | 0.75 | Tested |
| Lasso Regression | 0.74 | 0.74 | Tested |
| ElasticNet Regression | 0.74 | 0.74 | Tested |

**Final Model**

The **Gradient Boosting Regressor** delivered the highest **R² Score** and **Adjusted R²** among all evaluated models. Therefore, it was selected as the final model for deployment.

**Model Input**

- Age
- BMI
- Children
- Smoker (Yes / No)
- Gender (Male / Female)
- Region (Northeast, Northwest, Southeast, Southwest)

**Model Output**

- Predicted Medical Insurance Charges

**Project Structure**

```
Medical-Insurance-Cost-Prediction/
│
├── app.py
├── insurance.pkl
├── requirements.txt
├── README.md
└── insurance.csv
```
**Requirements**

Install all the required dependencies using:

```bash
pip install -r requirements.txt
```

**Application Preview**

The screenshot below shows the Streamlit web application used for predicting medical insurance charges.

![Streamlit Application](images/streamlit_app.png)
**Run the Project**

```bash
pip install -r requirements.txt
streamlit run app.py
```

**Future Improvements**

- Hyperparameter tuning
- Advanced feature engineering
- Interactive model comparison dashboard
- Improved Streamlit UI
- Cloud deployment

**Author**

**VIR**