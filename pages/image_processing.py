import streamlit as st
import cv2
import numpy as np
from PIL import Image

# 画像をアップロード
uploaded_file = st.file_uploader("画像をアップロード", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # PILで画像を読み込む
    image = Image.open(uploaded_file)

    # 画像をOpenCVの形式に変換
    image_np = np.array(image)
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # 画像を表示（OpenCVウィンドウ）
    cv2.imshow("Uploaded Image", image_cv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Streamlit上で画像を表示
    st.image(image, caption="アップロードされた画像", use_column_width=True)
