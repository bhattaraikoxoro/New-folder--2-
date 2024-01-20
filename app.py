from flask import Flask


from flask import Flask, request
# from flask_cors import CORS
# import joblib
import json

app = Flask(__name__)
# CORS(app)  # This will enable CORS for all routes
# CORS(app, origins="http://localhost:3000")


# @app.route('/predict', methods=['POST'])
# def predict():


@app.route("/")
def hello_world():
    return "<p>Fuck You!</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')