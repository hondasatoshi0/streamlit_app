import streamlit as st
import pandas as pd

# アップローダー
uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

# ファイル読み込み
if uploaded_file is not None:
  df = pd.read_csv(
    uploaded_file,
    sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
    engine='python',
    na_values='-',
    header=None
  )
