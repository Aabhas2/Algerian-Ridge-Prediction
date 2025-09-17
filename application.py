import numpy as np 
import pandas as pd 
import pickle as pkl
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# Import pickle files: Ridge regressor and standard scaler  
ridge_model = pkl.load(open("models/ridge.pkl","rb"))
standard_scaler = pkl.load(open("models/scaler.pkl","rb"))



@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == "POST":
        try:
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))

            new_data_scaled = standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
            result = ridge_model.predict(new_data_scaled)

            return render_template('home.html', results=round(float(result[0])*100, 2))
        except Exception as e:
            print("Error:", str(e))  # This will print the error in your console/logs
            return render_template('home.html', error="An error occurred during prediction. Please check your input values.")
         
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)