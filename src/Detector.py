from tensorflow.keras.applications.resnet50 import ResNet50
# Used for decoding predictions
from tensorflow.keras.applications.resnet50 import decode_predictions
from PIL import Image
import numpy as np


model = ResNet50(weights='imagenet')

def predict(image_path, IMG_SIZE=224):
    image = Image.open(image_path)
    # resize image to target size
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.asarray(image)
    image = np.expand_dims(image, axis=0)

    # Predict image using model
    resp = model.predict(image)
    # Get top predicted class label
    return decode_predictions(resp, top=1)[0][0]