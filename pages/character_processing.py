import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pytesseract

st.title("文字認識")

# 画像をアップロード
uploaded_file = st.file_uploader("画像をアップロード", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # PILで画像を読み込む
    image = Image.open(uploaded_file)

    # 画像をOpenCVの形式に変換
    image_np = np.array(image)
    # グレースケールに変換
    gray_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

    # ノイズの除去
    denoised = cv2.fastNlMeansDenoising(gray_image)

    # OCRによる文字認識
    text = pytesseract.image_to_string(Image.fromarray(denoised), lang='jpn')


    st.image(image_np, caption="画像", use_column_width=True)

    st.write("テキスト出力",text)

    uploaded_file = None
