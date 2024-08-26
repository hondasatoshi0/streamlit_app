import streamlit as st
import pandas as pd

# ページタイトルとページアイコン
st.title("Streamlit main")

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

# エラーメッセージ表示
if len(usecols) == 0 or len(names) == 0:
  st.error('解析対象の列が指定されていません。')
