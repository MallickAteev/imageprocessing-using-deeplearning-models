import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array

# Load the MobileNet model
model = MobileNet(weights="imagenet")

st.title("🖼️ Image Identifier with MobileNet")
st.write("Upload an image and I'll try to identify what's in it!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(image, channels="BGR", caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    image_resized = cv2.resize(image, (224, 224))
    image_array = img_to_array(image_resized)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = preprocess_input(image_array)

    # Predict
    preds = model.predict(image_array)
    label = decode_predictions(preds, top=1)[0][0]

    # Show result
    st.success(f"Prediction: **{label[1]}** ({label[2]*100:.2f}% confidence)")
