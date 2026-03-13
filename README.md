# Linear Regression from Scratch: Startup Revenue Predictor

An object-oriented Machine Learning engine built entirely from scratch in Python to predict startup revenue based on marketing spend. 

This project was developed to solidify the foundational mathematics of predictive AI. Instead of relying on high-level machine learning libraries like `scikit-learn` or `TensorFlow`, the core algorithm—calculating variance, covariance, and the line of best fit—is hardcoded using fundamental computer science logic and standard Python data structures.

## 🧠 The Architecture

The model is structured as a highly scalable Python class (`LinearRegression`), mirroring the architecture of professional AI libraries. 

* **`fit(x, y)`:** Ingests historical data, calculates the means, computes the variance and covariance, and establishes the optimal slope ($m$) and y-intercept ($b$) for the line of best fit.
* **`predict(new_x)`:** Accepts an array of unseen inputs and iterates through the calculated mathematical model to return a scalable list of predictions.
* **`calculate_mse()`:** Evaluates the model's accuracy using the Mean Squared Error mathematical formula to prove reliability.

## 📊 Real-World Business Application

In the startup and pitching ecosystem, forecasting growth is critical. This model analyzes a historical dataset of marketing expenditures and corresponding revenue to map a mathematically sound prediction trajectory. 

For the provided `startup_marketing.csv` dataset, the model successfully plotted the overarching growth trend, establishing a highly accurate predictive baseline with a Root Mean Squared Error (RMSE) of just ~$117 off actuals across the entire dataset.

## 🛠️ Tech Stack
* **Language:** Python
* **Core Concepts:** Object-Oriented Programming (OOP), Data Structures, Statistical Mathematics
* **Libraries:** `csv` (for native data ingestion), `matplotlib` (for visual data plotting)

## 🚀 How to Run Locally

1. Clone this repository to your local machine.
2. Ensure you have Python 3 installed.
3. Install the plotting library by running: `pip install matplotlib`
4. Execute the script: `python linear_regression.py`

The terminal will output the model's Mean Squared Error and a test prediction, followed by a graphical window displaying the scatter plot of historical data bisected by the model's calculated line of best fit.
