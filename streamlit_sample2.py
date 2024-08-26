import streamlit as st

st.write("# Streamlit sample2")

# 緯度経度データ（10進数）
pref_list = [
  {"longitude":135.161937, "latitude":33.894175}, # 本社
  {"longitude":135.139814, "latitude":33.89986}, # 美浜
  {"longitude":135.512259, "latitude":34.6832}, # 大阪支店
  {"longitude":139.757387,"latitude":35.666272}, # 東京営業所
  {"longitude":136.320687,"latitude":36.3034511}, # 北陸営業所
]

# 世界地図の表示
st.map(pref_list)
