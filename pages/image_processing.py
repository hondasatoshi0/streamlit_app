import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("画像処理")

# 画像をアップロード
uploaded_file = st.file_uploader("画像をアップロード", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # PILで画像を読み込む
    image = Image.open(uploaded_file)

    # 画像をOpenCVの形式に変換
    image_np = np.array(image)
    # グレースケールに変換
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    # エッジ
    edges_image = cv2.Canny(gray_image, 100 ,200)
    # コーナー
    corners_image = cv2.cornerHarris(gray_image, 2, 3, 0.04)

    # Streamlit上で画像を表示
    st.image(image_np, caption="リサイズされた画像", use_column_width=True)
    st.image(edges_image, caption="エッジ画像", use_column_width=True)
    st.image(corners_image, caption="コーナー画像", use_column_width=True)
