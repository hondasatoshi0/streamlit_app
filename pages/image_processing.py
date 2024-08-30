import streamlit as st
import cv2

st.title("画像処理")

# アップローダー
uploaded_file = st.file_uploader("アクセスログをアップロードしてください。",type="png")

st.write(uploaded_file)

image = cv2.imread(uploaded_file["name"])

cv2.imshow("Normal",image)
cv2.waitKey(0)
cv2.destroyAllWindows()