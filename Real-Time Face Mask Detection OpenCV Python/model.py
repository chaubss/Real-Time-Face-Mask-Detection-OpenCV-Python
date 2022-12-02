from tensorflow.keras.models import load_model

model = load_model('weights.20-0.17.h5')
# model = load_model('mask_detector.model')

model.summary()
