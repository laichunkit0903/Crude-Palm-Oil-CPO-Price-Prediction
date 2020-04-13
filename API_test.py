import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
import sys

# number of days chosen
print("Days of Prediction Chosen is : " +  str(sys.argv[1]) +" days" )

# test out the API created
url = 'http://localhost:5000/time_series'
r = requests.post(url, json ={"Day of Predictions" : str(sys.argv[1])})

# convert json result retrieved from API from and convert to data frame
df = pd.json_normalize(r.json())

# write the data frame result to CSV
df.to_csv("data_set/result/predicted_result_" + str(sys.argv[1]) + "days.csv" , index = False , )
print("Result Written To CSV successfully!" )