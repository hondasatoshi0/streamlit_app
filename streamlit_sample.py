import streamlit as st
import pandas as pd

# テキスト（マークダウンで書ける）
st.write("# tilte")

# 注釈
st.caption("注釈")

# 画像
st.image("サンプル.png")

# テーブル
df = pd.DataFrame(
  {
    "first colum": [1,2,3,4],
    "second column":[10,20,30,40],
  }
)
st.write(df)

# チャート
st.line_chart(df)
