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
    # リサイズ
    resize_image = cv2.resize(gray_image,(500,500))
    # エッジ
    edges_image = cv2.Canny(resize_image, 100 ,200)

    # Streamlit上で画像を表示
    st.image(edges_image, caption="画像処理", use_column_width=True)
