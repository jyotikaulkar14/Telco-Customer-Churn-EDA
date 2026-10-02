# Telco Customer Churn Analysis and Prediction

A machine learning project to analyze customer churn patterns and predict whether a telecom customer is likely to churn based on customer demographics, services, contract details, charges, and support-ticket information.

## Project Overview

Customer churn is an important challenge for telecom companies because losing customers can affect revenue and long-term growth.

This project analyzes a telecom customer dataset using Python and explores the factors associated with customer churn. Machine learning classification models are then trained to predict whether a customer is likely to churn.

The project includes exploratory data analysis, data preprocessing, model training, model evaluation, model comparison, feature importance analysis, and a customer churn prediction function.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Excel
- Joblib

## Project Workflow

1. **Data Loading**

   - Loaded the telecom customer churn dataset from Excel.
2. **Data Processing**

   - Converted `TotalCharges` into numeric format.
   - Handled missing values.
   - Separated input features and target variable.
   - Applied one-hot encoding to categorical features.
   - Applied standard scaling to numerical features.
3. **Train-Test Split**

   - Split the dataset into training and testing sets.
   - Used stratification to maintain the churn class distribution.
4. **Model Training**

   - Logistic Regression
   - Decision Tree
   - Random Forest
5. **Model Evaluation**

   - Accuracy
   - Precision
   - Recall
   - F1 Score
   - ROC-AUC
   - Confusion Matrix
   - Classification Report
   - ROC Curve
6. **Model Comparison**

   - Compared the performance of the three classification models using multiple evaluation metrics.
7. **Feature Importance**

   - Analyzed the features used by the Decision Tree for prediction.
8. **Churn Prediction**

   - Created a prediction function that accepts new customer information and returns a churn prediction and churn probability.

## Model Performance

| Model               | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| ------------------- | -------: | --------: | -----: | -------: | ------: |
| Logistic Regression |   85.81% |    75.89% | 68.18% |   71.83% |  92.76% |
| Decision Tree       |   85.38% |    72.46% | 72.46% |   72.46% |  91.16% |
| Random Forest       |   85.95% |    76.19% | 68.45% |   72.11% |  92.59% |

For the project's model-selection criterion, the Decision Tree was selected based on F1 Score. Its final evaluation on the test set achieved an F1 Score of 72.46% and ROC-AUC of 91.16%.

## Key EDA Insights

The exploratory data analysis identified several patterns associated with customer churn:

- Month-to-month contract customers showed a higher churn rate than customers with one-year or two-year contracts.
- Customers with shorter tenure showed higher churn compared with long-tenure customers.
- Customers who churned had higher average monthly charges than customers who did not churn.
- Fiber optic internet customers showed a higher churn rate than DSL and customers without internet service.
- Electronic check was associated with a higher churn rate among the payment methods.
- Customers without Online Security or Tech Support showed higher churn rates.
- Churned customers had a higher average number of technical support tickets.
- Senior citizens showed a higher churn rate than non-senior citizens.

## Feature Importance

The Decision Tree model identified the following features as the most important for churn prediction:

| Feature                             | Importance |
| ----------------------------------- | ---------: |
| tenure                              |   0.362739 |
| numTechTickets                      |   0.322718 |
| InternetService_Fiber optic         |   0.129118 |
| Contract_Two year                   |   0.059321 |
| TotalCharges                        |   0.050794 |
| StreamingMovies_No internet service |   0.024342 |
| InternetService_No                  |   0.020837 |
| MonthlyCharges                      |   0.012961 |
| MultipleLines_Yes                   |   0.008304 |
| PaymentMethod_Electronic check      |   0.004498 |

The feature importance values represent the relative contribution of each feature to the Decision Tree's splitting decisions. They should not be interpreted as causal effects.

## Project Structure

- `data/` — Dataset, processed data, trained models, preprocessing files, and results.
- `images/` — Project visualization images.
- `notebooks/` — Jupyter notebooks containing the complete analysis and machine learning workflow.
- `README.md` — Project documentation.

### Important Data and Model Files

- `Customer_Churn_Dataset.xlsx`
- `X_train_processed.csv`
- `X_test_processed.csv`
- `y_train_processed.csv`
- `y_test_processed.csv`
- `preprocessor.pkl`
- `logistic_regression_model.pkl`
- `decision_tree_model.pkl`
- `random_forest_model.pkl`
- `best_churn_model.pkl`
- `model_comparison_results.csv`
- `feature_importance.csv`

### Notebooks

- `02_Data_Processing.ipynb`
- `03_Train_Test_Split.ipynb`
- `04_Model_Training.ipynb`
- `05_Model_Evaluation.ipynb`
- `06_Multiple_Model_Training.ipynb`
- `07_Model_Comparison.ipynb`
- `08_Best_Model_Evaluation.ipynb`
- `09_Feature_Importance.ipynb`
- `10_Churn_Prediction_Function.ipynb`

## Prediction Example

The trained model can be used to predict churn for a new customer.

Example output from the prediction function:

**Prediction:** Yes

**Churn Probability:** 91.18%

**Result:** Customer is predicted to be at risk of churn.

The churn probability is the probability estimated by the trained Decision Tree model for the supplied customer input.

## How to Run the Project

### 1. Clone the repository

Run:

`git clone https://github.com/jyotikaulkar14/Telco-Customer-Churn-EDA.git`

Then:

`cd Telco-Customer-Churn-EDA`

### 2. Create a virtual environment

Run:

`python -m venv venv`

### 3. Activate the virtual environment

On Windows PowerShell, run:

`venv\Scripts\Activate.ps1`

### 4. Install required libraries

Run:

`pip install pandas numpy matplotlib seaborn scikit-learn openpyxl joblib jupyter`

### 5. Open the project

Open the project folder in VS Code and run the notebooks in the `notebooks` folder.

### 6. Run the notebooks in order

1. `02_Data_Processing.ipynb`
2. `03_Train_Test_Split.ipynb`
3. `04_Model_Training.ipynb`
4. `05_Model_Evaluation.ipynb`
5. `06_Multiple_Model_Training.ipynb`
6. `07_Model_Comparison.ipynb`
7. `08_Best_Model_Evaluation.ipynb`
8. `09_Feature_Importance.ipynb`
9. `10_Churn_Prediction_Function.ipynb`

## Author

**Jyoti Kaulkar**

Data Science Student

GitHub: [@jyotikaulkar14](https://github.com/jyotikaulkar14)
