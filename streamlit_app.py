import streamlit as st
import pandas as pd

# アップローダー
uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

# ファイル読み込み
if uploaded_file:
  df = pd.read_csv(uploaded_file)

st.markdown('### 内容表記')
st.write(df.head(5))

# ページタイトルとページアイコン
st.set_page_config(page_title="メインページ",page_icon="icon.png")
st.title("Streamlit テストページ")
