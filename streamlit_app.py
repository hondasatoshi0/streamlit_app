import streamlit as st
import pandas as pd

# アップローダー
uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

st.markdown('### 内容表記')

# ファイル読み込み
if uploaded_file:
  df = pd.read_csv(uploaded_file)
  st.write(df.head(5))



# ページタイトルとページアイコン
st.set_page_config(page_title="メインページ")
st.title("Streamlit テストページ")
