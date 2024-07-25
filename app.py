from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the pre-trained model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        request.form.get('fixed_acidity'),
        request.form.get('volatile_acidity'),
        request.form.get('citric_acid'),
        request.form.get('residual_sugar'),
        request.form.get('chlorides'),
        request.form.get('free_sulfur_dioxide'),
        request.form.get('total_sulfur_dioxide'),
        request.form.get('density'),
        request.form.get('sulphates'),
        request.form.get('alcohol'),
        request.form.get('quality')
    ]
    features = [float(x) for x in features]
    features_array = np.array([features])
    prediction = model.predict(features_array)
    return render_template('index.html', prediction_text=f'The predicted pH is {prediction[0]:.2f}')

if __name__ == "__main__":
    app.run()