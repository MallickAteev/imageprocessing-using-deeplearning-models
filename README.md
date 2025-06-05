# 🖼️ Image Identifier Web App using Streamlit and MobileNet

This is a simple and interactive web application built with [Streamlit](https://streamlit.io/) that uses the pre-trained [MobileNet](https://keras.io/api/applications/mobilenet/) model to identify objects in uploaded images.

<br/>

## 🚀 Features

- Upload any `.jpg`, `.jpeg`, or `.png` image
- The app will classify the image and display the **predicted object** along with the **confidence score**
- Runs entirely in your browser — no need for any special software (if deployed)

<br/>

## 🧠 How It Works

- **Streamlit** provides the web interface to upload and display images
- **MobileNet**, a lightweight neural network pre-trained on ImageNet, is used to classify the image
- The model returns the top prediction with the object name and probability

<br/>

## 📸 Demo Screenshot

![Demo](demo_screenshot.png)

> Replace with your own screenshot if you have one

<br/>

## 🛠️ Installation & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/image-identifier-app.git
cd image-identifier-app
