import streamlit as st

st.write("# Streamlit sample2")

# 緯度経度データ（10進数）
pref_list = [
  {"longitude":130.741667, "latitude":32.789828}, # 熊本県
  {"longitude":131.423855, "latitude":31.911090}, # 宮崎県
  {"longitude":130.557981, "latitude":31.560148}, # 鹿児島県
]


# 世界地図の表示
st.map(pref_list)
