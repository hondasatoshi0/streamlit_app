import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# サイドバー設定
st.sidebar.page_link("main.py", label="ホーム",icon="🏠")
st.sidebar.write("### 処理")
st.sidebar.page_link("pages/image_processing.py",label="画像処理",icon="📷")
st.sidebar.page_link("pages/character_processing.py",label="文字認識",icon="🔤")
st.sidebar.page_link("pages/graph_plotting.py",label="グラフ表示",icon="📈")

#
st.write("# グラフ表示")

st.write('### グラフ１')
chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["い","ろ","は"])
st.line_chart(chart_data)

st.write('### グラフ２')
# 画像をアップロード
uploaded_file = st.file_uploader("テキスト形式ファイルをアップロード", type=["txt", "csv"])

if uploaded_file is not None:
    data_fream = pd.csv_reader(uploaded_file,header = 1, names=(("Date and time","実績ショット数")))
    st.line_chart(data_fream)
