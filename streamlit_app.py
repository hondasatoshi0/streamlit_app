import streamlit as st
import pandas as pd

# ページタイトルとページアイコン
st.title("Streamlit テストページ")

# アップローダー
uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

st.markdown('### 内容表記')

# ファイル読み込み
if uploaded_file:
  df = pd.read_csv(uploaded_file)
  st.write(df.head(5))

usecols = st.multiselect(
  '何番目の列を解析の対象にしますか？',
  [0, 3, 4, 5, 6],
  [0, 3, 4, 5, 6]
)
