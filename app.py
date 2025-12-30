from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np

app = Flask(__name__)

# Load the trained model
model = load_model('model/Brain-Tumor-Detection-ADILKHAN2.h5')

# Function to preprocess the image before making predictions
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        img_path = 'uploads/' + file.filename
        file.save(img_path)
        
        # Preprocess the image
        img_array = preprocess_image(img_path)

        # Make prediction
        prediction = model.predict(img_array)
        result = {'class': int(np.round(prediction[0][0])), 'class_name': 'Tumor' if prediction > 0.5 else 'Normal'}

        # Add the prediction to the response
        result['prediction'] = result['class_name']

        return render_template('index.html', prediction_text=result['prediction'])

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
