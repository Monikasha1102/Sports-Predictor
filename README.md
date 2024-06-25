# Sports-Predictor

# Overview

Sports Predictor is a Python application that uses machine learning to predict the outcomes of sports matches. Featuring a user-friendly GUI built with Tkinter, it allows users to select teams and venues, leveraging historical match data to generate predictions using a Random Forest Classifier.

# Features

User-Friendly Interface: Built with Tkinter, the GUI allows easy selection of teams and venues for prediction.

Machine Learning: Uses Random Forest Classifier for making predictions.

Data Handling: Efficient preprocessing of historical data with Pandas and scikit-learn for label encoding.

# Usage

## First Window 

Click "START" to proceed to the prediction window.

<img width="676" alt="window1" src="https://github.com/Monikasha1102/Sports-Predictor/assets/173608236/4a0cbb6a-965c-4d6d-ae9d-9d299ba0105c">

## Prediction Window

Select teams and venue from the dropdown menus and click "Predict" to see the result.

<img width="678" alt="window2" src="https://github.com/Monikasha1102/Sports-Predictor/assets/173608236/84678384-8280-4721-a122-dd01ea29795a">

## Final Output

<img width="675" alt="outputwindow" src="https://github.com/Monikasha1102/Sports-Predictor/assets/173608236/359c2f9d-45a9-45be-a745-4236d8a04cfa">

# Project Structure 

code.py: Main script.
deliveries.csv and matches.csv: Dependencies file.

# Data Preprocessing

Historical match data is preprocessed using Pandas.
Label encoding is used to convert categorical data into numerical values.
The Random Forest model is trained on the preprocessed data to make predictions.

# conclusion

The Sports Predictor project successfully combines machine learning with a user-friendly interface to provide accurate predictions for sports matches. By leveraging historical match data and the robust Random Forest Classifier, the application offers users an insightful tool for forecasting game outcomes. The intuitive GUI built with Tkinter ensures that users can easily interact with the application, making it accessible even to those without a technical background.

This project not only demonstrates the practical application of machine learning techniques in sports analytics but also highlights the importance of data preprocessing and feature engineering. The effective use of Pandas and scikit-learn for data handling ensures that the model is trained on clean, relevant data, enhancing its predictive accuracy.




