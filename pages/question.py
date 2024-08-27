import streamlit as st
import datetime
import re

st.write("# 依頼書フォーム")

# 部署
section = st.selectbox("所属部署", ["製造１課","製造２課","製造３課","エンジニアリング部","押出課","その他"], index = None, placeholder = "所属部署を選択してください。")

# 氏名
if "name" not in st.session_state:
  st.session_state.name = ""
  
name_input = st.text_input("氏名　※空白を空けずに入力してください。")

if name_input is not None:
  name_split = re.split("[; :　/]",name_input)
  for i in range(len(name_split)):
    st.session_state.name = st.session_state.name + name_split[i]



# 依頼内容
request = st.text_input("依頼内容　※最大200文字", max_chars = 200)

# ファイルアップロード
st.write("写真や資料があればこちらからアップロードしてください。※１つまで")
uploaded_file = st.file_uploader("アップロード")

# 依頼詳細１
request_detail1 = st.text_input("製品の品質に関する注意事項内容又は要望　※最大200文字", max_chars = 200)

# 依頼詳細２
request_detail2 = st.text_input("動作に関する注意事項又は要望　※最大200文字", max_chars = 200)

# 依頼詳細３
request_detail3 = st.text_input("そのほかの注意事項内容又は要望　※最大200文字", max_chars = 200)

# 希望納期
d = st.date_input("希望納期を入力してください。",datetime.datetime.now())
