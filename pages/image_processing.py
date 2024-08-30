import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("画像処理")

# 画像をアップロード
uploaded_file = st.file_uploader("画像をアップロード", type=["jpg", "png", "jpeg"])

if st.button("実行"):
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
        img_dst = np.copy(gray_image)
        dst = cv2.cornerHarris(gray_image, 2, 3, 0.04, img_dst)
        dst = cv2.dilate(dst,None,iterations=3)

        corners_image = np.copy(image_np)
        corners_image[dst>0.05*dst.max()] = [0,0,255]

        cols1 = st.columns(2)
        with cols1[0]:
            st.image(image_np, caption="リサイズされた画像", use_column_width=True)
        with cols1[1]:
            st.image(gray_image, caption="グレー画像", use_column_width=True)


        cols2 = st.columns(2)
        with cols2[0]:
            st.image(edges_image, caption="エッジ画像", use_column_width=True)
        with cols2[1]:
            st.image(corners_image, caption="コーナー画像", use_column_width=True)
    else:
        st.error("実行できませんでした。画像をアップロードしてください。")
