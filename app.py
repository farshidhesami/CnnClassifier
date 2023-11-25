from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils import decodeImage
from cnnClassifier.pipeline.predict import DogCat
import logging

# Set environment variables
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Use environment variables for configuration
filename = os.getenv('INPUT_IMAGE', 'inputImage.jpg')

class ClientApp:
    def __init__(self):
        self.filename = filename
        self.classifier = DogCat(self.filename)

@app.route("/", methods=['GET'])                      # Render HTML page   
@cross_origin()
def home():
    return render_template('index.html')              

@app.route("/train", methods=['GET','POST'])          # Training methods        
@cross_origin()
def trainRoute():
    try:
        os.system("python main.py")
        logging.info("Training done successfully")
        return "Training done successfully!"
    except Exception as e:
        logging.error(f"An error occurred during training: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/predict", methods=['POST'])              # Predict methods
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictiondogcat()
    return jsonify(result)

if __name__ == "__main__":                            # Initialize "post" and "put"
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)