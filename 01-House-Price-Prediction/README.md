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
