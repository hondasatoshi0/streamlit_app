import streamlit as st
import pandas as pd

# ページタイトルとページアイコン
st.title("Streamlit main")

# ページリンク
st.write("### サンプル")
st.page_link("pages/streamlit_sample.py", label="sample 1",icon="1⃣")
st.page_link("pages/streamlit_sample2.py", label="sample 2",icon="2⃣")
st.page_link("pages/requestForm.py", label="依頼書フォーム",icon="🌟")
st.page_link("pages/requestData.py", label="依頼一覧",icon="🌟")

# アップローダー
uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

st.markdown('### 内容表記')

# ファイル読み込み
if uploaded_file:
  df = pd.read_csv(uploaded_file)
  st.write(df.head(5))

# 列選択のためのウィジェット
usecols = st.multiselect(
  '何番目の列を解析の対象にしますか？',
  [0, 3, 4, 5, 6],
  [0, 3, 4, 5, 6]
)

# 世界地図の表示
st.map()
