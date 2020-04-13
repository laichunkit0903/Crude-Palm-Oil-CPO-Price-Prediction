# Crude-Palm-Oil-CPO-Price-Prediction
This repository contained  analysis for possible features that might affect crude palm oil (CPO) price and steps to buld up time series model to build the prediction mdoel.

This repository consisted of 3 jupyer notebooks, 1 python file , 1 time series model , 1 flask apps folder and 1 dockerize falsk apps folder.
 <br>
# Jupyter Notebook:
1. Transform Raw Data and Save to CSV and Database - Consist of Steps to transform the data and save to CSV and database.
2. Correlation Analysis - Consists of steps to analyze possible features that could affect the CPO price.
3. Time Series Predicitn Model - Consists of steps in bulding time series prediction model using Python FBProphet package.

# Flask_Apps folder:
1. CD to the folder and run python.appy to activate the Time Series Model API which build with Python Flask.
2. URL link is http//:0.0.0.0:5000/time_series 
3. Could run API_test.py file to test out the API once is up by running python API_test.py x where x is number of days of predicitons.
4. Or could use postman to test out by posting {"Day of Prediction" : "x"} as input where x is number of days of predicitons.

# Dockerzie_Flask:
1. This folder contained dockerized Time Series Model API which build with Python Flask.
2. This docker file could be build and deployed.
