from flask import Flask
from flask import request
from flask import render_template

import pickle

#Personnal function 

from data_preprocessing.preprocessing_users_data import convert_request_form_into_dict_flask
from data_preprocessing.fitting_data_model import fitting_data_model_flask
from modeling.modeling import modeling

#Path of the file with the dataframe with the columns the model needs
features_path = "modeling/models/X_form.pkl"
#Loading the pkl file containing a df with the columns used by the ML engineer in his model
df_features = pickle.load(open(features_path, "rb"))

app = Flask(__name__)

@app.route("/", methods=['GET'])
def first_page():
    if request.args.get :
        return render_template("getting_data.html")

@app.route("/prediction", methods=['POST'])
def prediction():
    # Converting the data received from the form into a classical dict to store them clearly
    received_data : dict = convert_request_form_into_dict_flask()
    print(received_data)
    
    # Preprocessing the data for them to fit the data needed to enter into the model
    data_fit_model : list = fitting_data_model_flask(received_data, df_features)
    print(f"{data_fit_model} is {len(data_fit_model)} length")
    #print(df_features)
    total = 0
    for i, el in enumerate(data_fit_model):
        if el > 0 :
            print(f"the column {i} is fullfilled with the value {el}")
            total += 1
    print(total)

    predict_churn = modeling(data_fit_model)

    return render_template("prediction_result.html", prediction_result=predict_churn)

if __name__ == "__main__":
    # Running the app on port 5000, in debugging mode (interactive terminal) and most important thing the host here and not in the Dockerfile !!!
    app.run(port=4999, debug=True, host="0.0.0.0")