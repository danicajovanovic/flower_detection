from pathlib import Path
from PIL import Image
import streamlit as st
from ultralytics import YOLO


BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "models" / "best.pt"


@st.cache_resource
def load_model():
    return YOLO(str(MODEL_PATH))


st.set_page_config(
    page_title="Flower Detection",
    page_icon="🌸",
    layout="centered"
)

st.title("🌸 Flower Detection")
st.write(
    "Upload an image and the model will detect and classify flowers."
)

model = load_model()

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

confidence = st.slider(
    "Confidence threshold",
    0.1,
    1.0,
    0.25,
    0.05
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Original image")
    st.image(image, use_container_width=True)

    if st.button("Run detection"):

        results = model.predict(
            source=image,
            conf=confidence
        )

        output = results[0].plot()

        st.subheader("Detection result")
        st.image(output, use_container_width=True)

        if len(results[0].boxes) > 0:

            st.subheader("Detected objects")

            for box in results[0].boxes:
                class_id = int(box.cls[0])
                class_name = model.names[class_id]
                score = float(box.conf[0])

                st.write(
                    f"• {class_name} ({score:.2f})"
                )

        else:
            st.warning("No flowers detected.")