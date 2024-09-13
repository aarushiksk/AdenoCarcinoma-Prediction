import streamlit as st
from ChestCancerClassifier.utils.common import decodeImage
from ChestCancerClassifier.pipeline.prediction import PredictionPipeline
from PIL import Image
import base64

# Initialize the classifier
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

clApp = ClientApp()

def main():
    st.title("Chest Cancer Classifier")
    st.text("Upload a chest X-ray image for image classification as cancerous or non-cancerous")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Save the uploaded file
        with open(clApp.filename, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Display the uploaded image
        # image = Image.open(uploaded_file)
        # st.image(image, caption='Uploaded Image.', use_column_width=True)

        # Encode the image to base64
        with open(clApp.filename, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')

        # Decode the image and make a prediction
        decodeImage(base64_image, clApp.filename)
        result = clApp.classifier.predict()

        # Display the prediction result
        st.write("## Prediction Result")
        st.write(result)
    # Optionally, you can add a button to trigger the prediction
    if st.button('Predict'):
        if uploaded_file is not None:
            # Encode the image to base64
            with open(clApp.filename, "rb") as image_file:
                base64_image = base64.b64encode(image_file.read()).decode('utf-8')

            decodeImage(base64_image, clApp.filename)
            result = clApp.classifier.predict()
            st.write("## Prediction Result")
            st.write(result.get('image', 'No image key found'))
        else:
            st.write("Please upload an image first.")

if __name__ == "__main__":
    main()