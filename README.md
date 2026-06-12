# 🚗 Car Price Prediction using Machine Learning

## Project Overview

This project predicts the selling price of used cars using Machine Learning.

The dataset contains information about:

* Car Brand
* Fuel Type
* Transmission
* Owner Type
* Seller Type
* Kilometers Driven
* Manufacturing Year

The model was trained using Linear Regression after performing data cleaning, feature engineering, encoding, and outlier treatment.

---

## Dataset

Car Details Dataset (CarDekho)

Features:

* Year
* KM Driven
* Fuel Type
* Seller Type
* Transmission
* Owner Type
* Brand

Target:

* Selling Price

---

## Data Preprocessing

* Removed duplicate records
* Created Car Age feature
* Applied One-Hot Encoding
* Handled skewed distribution using Log Transformation
* Feature Engineering performed

---

## Exploratory Data Analysis

### Correlation Heatmap

Understanding relationships among variables.

### Outlier Detection

Boxplots were used to detect extreme values.

### 3D Visualization

Visualized the relationship between:

* Car Age
* KM Driven
* Selling Price

---

## Model Used

Linear Regression

Performance:

* R² Score: 0.767
* Adjusted R² Score: 0.755

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Streamlit

---

## Streamlit Deployment

The project includes a Streamlit web application where users can:

* Select Car Brand
* Choose Fuel Type
* Choose Transmission
* Enter Car Age
* Enter KM Driven

And receive a predicted selling price.

---

## Author

Sushant
