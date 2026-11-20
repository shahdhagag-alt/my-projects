import streamlit as st
from PIL import Image
from transformers import pipeline

st.set_page_config(page_title="Food Classifier", page_icon="🍕", layout="centered")

st.title("🍕 Food Classifier")
st.write("Upload a photo of food and the model will guess what it is.")


# بنحمّل الموديل مرة واحدة بس عشان التطبيق ميبقاش بطيء
@st.cache_resource(show_spinner="Loading model... (first time takes a few minutes)")
def load_model():
    return pipeline("image-classification", model="nateraw/food")


classifier = load_model()

uploaded = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Your image", use_container_width=True)

    with st.spinner("Thinking..."):
        results = classifier(image, top_k=3)

    best = results[0]
    st.success(f"I think this is: **{best['label'].replace('_', ' ')}** ({best['score']:.0%})")

    st.subheader("Top 3 guesses")
    for r in results:
        st.write(r["label"].replace("_", " ").title())
        st.progress(float(r["score"]))
