# Salary Prediction using Multiple Linear Regression

A beginner Machine Learning project that predicts an employee's salary using **Multiple Linear Regression** with **scikit-learn**.

This project demonstrates how multiple independent variables can be used together to estimate a continuous target value. The model predicts salary based on an individual's **years of experience**, **written test score**, and **interview score**.

---

## Project Overview

The objective of this project is to understand how Multiple Linear Regression models the relationship between several input features and a target variable.

The model predicts an employee's salary using the following factors:

* Years of Experience
* Test Score (out of 10)
* Interview Score (out of 10)

---

## Dataset

The dataset contains the following features:

| Column                       | Description                      |
| ---------------------------- | -------------------------------- |
| `experience`                 | Years of professional experience |
| `test_score(out of 10)`      | Written test score out of 10     |
| `interview_score(out of 10)` | Interview score out of 10        |
| `salary($)`                  | Salary (target variable)         |

---

## Machine Learning Workflow

* Load and inspect the dataset using Pandas.
* Convert textual values (e.g., "five") into numerical values using the **word2number** library.
* Handle missing values.
* Prepare the input features and target variable.
* Train a Multiple Linear Regression model.
* Predict salaries for new candidates.
* Analyze the learned coefficients and intercept.
* Verify predictions using the trained model.

---

## Output

The notebook demonstrates:

* Data preprocessing
* Handling missing values
* Model training
* Salary prediction
* Interpretation of model coefficients

---

## Model Evaluation

The model was evaluated using a train-test split after preprocessing the dataset (handling missing values and converting textual numerical values using the **word2number** library).

| Metric                             |             Value |
| ---------------------------------- | ----------------: |
| **R² Score**                       |        **0.5932** |
| **Mean Absolute Error (MAE)**      |  **7,838.98 USD** |
| **Mean Squared Error (MSE)**       | **73,918,701.52** |
| **Root Mean Squared Error (RMSE)** |  **8,597.60 USD** |

The model achieved an **R² Score of 0.5932**, indicating that it explains approximately **59.32% of the variation** in salary based on the candidate's experience, test score, and interview score. Due to the small size of the dataset, the evaluation metrics are sensitive to the train-test split and should be interpreted as part of a learning exercise rather than a definitive measure of real-world model performance.


## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook
* Word2Number

---

##  How to Run

Clone the repository:

```bash
git clone <repository-url>
cd multiple-linear-regression/02-Salary-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open `salary_prediction.ipynb` and run all the cells.

---

## Results

The trained Multiple Linear Regression model successfully predicts salary based on multiple input features. The notebook demonstrates how experience, test performance, and interview performance influence the final salary prediction through the learned regression coefficients.

---

## Learning Outcomes

Through this project I learned:

* Converting textual numerical values into integers using the word2number library.
* Handling missing values before training a model.
* Working with multiple independent variables.
* Training a Multiple Linear Regression model using scikit-learn.
* Understanding regression coefficients and the intercept.
* Making predictions for unseen data.
* Organizing a Machine Learning project using a clean GitHub structure.
* Evaluate model performance using metrics such as **R² Score**, **Mean Squared Error (MSE)**, and **Mean Absolute Error (MAE)**.
  
---

## Future Improvements

* Train the model on a larger real-world salary dataset.
* Explore additional features such as education level, job role, location, and technical skills.
* Compare Multiple Linear Regression with other regression algorithms.

---
