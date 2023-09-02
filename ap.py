from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Load the Random Forest Classifier model
filename = "C:\\Users\\oordv\\mod.pkl"
model = pickle.load(open(filename, "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST","GET"])
def predict():
    if request.method == "POST":
        input_features = [float(x) for x in request.form.values()]
        # Make prediction using the loaded model
        my_prediction = model.predict([input_features])
        # Convert prediction to a human-readable result

    return render_template("result.html", prediction=my_prediction)
        

if __name__ == "__main__":
    app.run(debug=False)
