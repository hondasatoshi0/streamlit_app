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