import streamlit as st
import time

# サイドバーにページリンクを非表示
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] ul {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.page_link("main.py", label="ホーム",icon="🏠")

try:
  if not st.session_state['authenticated']:
    st.page_link("main.py",label="ログインページへ",icon="🏠")
  else:
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
    st.map(pref_list,size=1)


    # プログレスバー
    my_bar = st.progress(0)
    for i in range(0,100):
      time.sleep(0.1)
      my_bar.progress(i+1)
except KeyError:
  st.page_link("main.py",label="ログインページへ",icon="🏠")