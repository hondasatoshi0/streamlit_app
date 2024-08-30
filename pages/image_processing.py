import streamlit as st
import cv2
import numpy as np

st.title("画像処理")

# アップローダー
file_path = st.file_uploader("画像をアップロードしてください。",type=["png","jpg","jpeg"])

if file_path:
    image_bytes = file_path.read()

    image = cv2.imdecode(np.frombuffer(image_bytes, np.unit8), cv2.IMREAD_COLOR)

    st.image(image, channels="BGR")