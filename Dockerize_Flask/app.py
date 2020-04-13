from flask import Flask, jsonify, request, render_template,  session, redirect
from flask_cors import CORS, cross_origin
import fbprophet
import joblib
import pandas as pd

# Load the saved time series model
filename = 'time_series.sav'
loaded_model = joblib.load(filename)

# Creating a flask app
app = Flask(__name__)


CORS(app)
@app.route("/time_series", methods=['GET','POST'])
def predict():

	#if the fucntion in post method
	if request.method == 'POST':
		horizon = int(request.json['Day of Predictions'])

		# Fit in loaded model and make prediction based on number of days input
		future = loaded_model.make_future_dataframe(periods=horizon, freq='D')

		# Load soybean data as extra regression for the model
		soybean_df = pd.read_csv("BO1 COMB Comdty.csv" , low_memory = False)
		soybean_df = soybean_df.dropna()
		future['soybean'] = soybean_df['BO1 COMB Comdty_PX_LAST']
		forecast = loaded_model.predict(future)

		# Extract the predicted period
		data = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-horizon:]

		# Convert results to json format
		ret = data.to_json(orient='records', date_format='iso')
		return ret

if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0')