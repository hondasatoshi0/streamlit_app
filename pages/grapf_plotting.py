import streamlit as st
import pandas as pd
import numpy as np

st.title = ("グラフ表示")

chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["い","ろ","は"])

st.line_chart(chart_data)