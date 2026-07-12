# House Price Prediction using Multiple Linear Regression

A beginner Machine Learning project that predicts house prices using **Multiple Linear Regression** with **scikit-learn**.

Unlike Simple Linear Regression, this project uses **multiple input features** to estimate the price of a house, making the predictions more realistic and accurate.

---

## Project Overview

The objective of this project is to understand how Multiple Linear Regression can model the relationship between several independent variables and a single target variable.

The model predicts the selling price of a house based on:

* Area (square feet)
* Number of bedrooms
* Age of the house

---

## Dataset

The dataset contains the following features:

| Column    | Description                   |
| --------- | ----------------------------- |
| `area`    | Area of the house (sq. ft.)   |
| `bedroom` | Number of bedrooms            |
| `age`     | Age of the house (years)      |
| `price`   | House price (target variable) |

---

## Machine Learning Workflow

* Load and inspect the dataset using Pandas.
* Handle missing values (if any).
* Select multiple input features.
* Train a Multiple Linear Regression model.
* Predict house prices for unseen data.
* Understand model coefficients and intercept.
* Verify predictions manually using the regression equation.

---

## Output

The notebook demonstrates:

* Training a Multiple Linear Regression model.
* Predicting house prices using multiple features.
* Interpreting model coefficients.
* Comparing manual calculations with model predictions.

## Model Evaluation

The model was evaluated using a train-test split to demonstrate the model evaluation workflow.

| Metric                             |                Value |
| ---------------------------------- | -------------------: |
| **R² Score**                       |            **-0.09** |
| **Mean Absolute Error (MAE)**      |    **61,003.75 USD** |
| **Mean Squared Error (MSE)**       | **7,570,217,633.65** |
| **Root Mean Squared Error (RMSE)** |    **87,007.00 USD** |

The evaluation metrics indicate that the model did not generalize well on the test set for this particular train-test split. This is expected because the dataset contains only **five samples** while the model is trained using **three input features** (area, number of bedrooms, and house age). With such a limited dataset, the evaluation metrics are highly sensitive to the train-test split and should be interpreted as a demonstration of the evaluation process rather than a measure of real-world model performance.

Despite the limited dataset, this project successfully demonstrates key concepts of Multiple Linear Regression, including:

* Data preprocessing and handling missing values using median imputation.
* Training a Multiple Linear Regression model with multiple input features.
* Understanding regression coefficients and the intercept.
* Making predictions for unseen inputs.
* Evaluating model performance using common regression metrics such as R² Score, MAE, MSE, and RMSE.


## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook

---

##  How to Run

Clone the repository:

```bash
git clone <repository-url>
cd multiple-linear-regression/01-House-Price-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open `house_price_prediction.ipynb` and run all cells.

---

## Results

The trained model successfully learns how multiple factors influence house prices.

The notebook demonstrates:

* Model training
* Price prediction
* Coefficient analysis
* Manual verification of predictions using the regression equation

---

## Learning Outcomes

Through this project I learned:

* The difference between Simple and Multiple Linear Regression.
* Working with multiple independent variables.
* Training regression models using scikit-learn.
* Understanding regression coefficients and intercept.
* Predicting values using both the model and the regression equation.
* Organizing a Machine Learning project following GitHub best practices.

---

## Future Improvements

* Evaluate the model using performance metrics such as **R² Score** and **Mean Squared Error (MSE)**.
* Train and test the model on a larger real-world housing dataset.
* Experiment with additional features such as location, number of bathrooms, parking spaces, and nearby amenities.
* Compare Multiple Linear Regression with other regression algorithms to analyze prediction performance.
