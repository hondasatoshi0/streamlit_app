import streamlit as st

st.write("# 依頼書フォーム")

# 部署
section = st.selectbox("所属部署を選択してください。",["製造１課","製造２課","製造３課","エンジニアリング部","押出課","その他"],placeholder="...")

# 氏名
name = st.text_input("氏名　※空白を空けずに入力してください。")

