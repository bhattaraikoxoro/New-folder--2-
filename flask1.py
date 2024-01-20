from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import json

app = Flask(__name__)
CORS(app)

# Load the model
model = joblib.load('model_confidence.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)
    print("Received data:", data)

    # Make prediction using the model loaded
    prediction = model.predict([list(data.values())])
    print("Prediction:", prediction)

    # Take the first value of prediction
    output = prediction[0]

    # Return the data and prediction in the response
    response_data = {
        "data": data,
        "prediction": prediction.tolist()  # Convert prediction to a list for JSON serialization
    }

    return jsonify(response_data)

if __name__ == '__main__':
    # app.run(port=5000, debug=True)\
    app.run(debug=True, host='0.0.0.0', port=5000)