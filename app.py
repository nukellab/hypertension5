
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Hemoglobin =float(request.form['Hemoglobin'])
            G_P_C = float(request.form['G_P_C'])
            Age = float(request.form['Age'])
            BMI = float(request.form['BMI'])
            Gender = float(request.form['Gender'])
            Pregnancy = float(request.form['Pregnancy'])
            Smoking = float(request.form['Smoking'])
            Phy_act = float(request.form['Phy_act'])
            salt_content = float(request.form['salt_content'])
            alcohol_cons = float(request.form['alcohol_cons'])
            Stress = float(request.form['Stress'])
            kidney_disease = float(request.form['kidney_disease'])
            thyroid_disord = float(request.form['thyroid_disord'])

            filename = 'randomforestclassifier.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[Hemoglobin,G_P_C,Age,BMI,Gender,Pregnancy,Smoking,Phy_act,salt_content,alcohol_cons,Stress,kidney_disease,thyroid_disord]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction=round(100 * prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
	app.run(debug=True) # running the app