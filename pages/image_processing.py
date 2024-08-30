import streamlit as st
import cv2
import numpy as np

st.title("画像処理")

# アップローダー
file_path = st.file_uploader("画像をアップロードしてください。",type=["png","jpg","jpeg"])

image = cv2.imread(file_path.name)

st.image(image)