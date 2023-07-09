import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model


classes = ['猫', 'ライオン', 'チーター']

def predict(X):
    """
    モデルのロード

    """
    model = load_model('ai/catai_cnn_new.h5')
    result = model.predict([X])[0]
    predicted = result.argmax()
    return str(classes[predicted])
