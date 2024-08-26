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


