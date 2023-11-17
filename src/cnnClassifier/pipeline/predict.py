import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class DogCat:                                                                  # Define a DogCat class
    def __init__(self,filename):
        self.filename =filename

    def predictiondogcat(self):                                                # Define a predictiondogcat
        
        model = load_model(os.path.join("artifacts","training", "model.h5"))   # For load a model in path

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224)) # Base on IMAGE_SIZE: [224, 224, 3] in "params.yaml"
        test_image = image.img_to_array(test_image)                     # Convert image to np
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:                                                      # If equal to 1 prediction is dog
            prediction = 'dog'
            return [{ "image" : prediction}]                                    # Prediction in jason format
        else:
            prediction = 'cat'
            return [{ "image" : prediction}]