from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import io
import tensorflow as tf

app = Flask(__name__)

# Load your pre-trained model
# Replace 'path/to/your/model' with the actual path to your model
model = tf.keras.models.load_model('path/to/your/model')

# Define a function to preprocess the image before feeding it to the model
def preprocess_image(image):
    # Resize the image to match the input size expected by the model
    image = image.resize((224, 224))
    # Convert the image to a numpy array
    image_array = np.asarray(image)
    # Normalize the image values to the range [0, 1]
    normalized_image_array = (image_array.astype(np.float32) / 255.0)[np.newaxis, ...]
    return normalized_image_array

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the request contains an image file
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    # Read the image from the request
    image_file = request.files['image']
    image = Image.open(io.BytesIO(image_file.read()))

    # Preprocess the image
    processed_image = preprocess_image(image)

    # Make predictions using the loaded model
    predictions = model.predict(processed_image)

    # Assuming your model outputs three probabilities for fire, deforestation, and animals
    fire_prob, deforestation_prob, animals_prob = predictions[0]

    # You can customize the response format based on your requirements
    response = {
        'fire_probability': float(fire_prob),
        'deforestation_probability': float(deforestation_prob),
        'animals_probability': float(animals_prob)
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
