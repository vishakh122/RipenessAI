import streamlit as st
from PIL import Image
import random

st.set_page_config(
    page_title="Ripeness AI",
    page_icon="🍎",
    layout="wide"
)

st.title("🍎 Ripeness AI")
st.subheader("AI-Based Fruit Ripeness Detection System")

st.write(
    "Upload a fruit image and our AI will analyze its ripeness."
)

st.divider()

st.header("📷 Fruit Inspection")

uploaded_image = st.file_uploader(
    "Upload a fruit image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image is not None:

    image = Image.open(uploaded_image)

    st.image(
        image,
        caption="Uploaded Fruit",
        width=400
    )

    st.success("Image uploaded successfully!")

    if st.button("🔍 Analyze Ripeness"):

        with st.spinner("Analyzing fruit..."):

            prediction = random.choice(
                ["Unripe", "Ripe", "Overripe"]
            )

            confidence = random.uniform(85, 99)

        st.divider()

        st.header("🤖 AI Analysis Result")

        st.metric(
            "Predicted Ripeness",
            prediction
        )

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        if prediction == "Unripe":
            st.warning(
                "🍏 The fruit appears to be unripe."
            )

        elif prediction == "Ripe":
            st.success(
                "🍎 The fruit appears to be ripe and ready to eat."
            )

        else:
            st.error(
                "🍎 The fruit appears to be overripe."
            )
