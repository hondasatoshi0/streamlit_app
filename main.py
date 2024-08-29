import streamlit as st
import pandas as pd

import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# ページタイトルとページアイコン
st.title("Streamlit main")

# ページリンク
st.write("### サンプル")
st.page_link("pages/streamlit_sample.py", label="sample 1",icon="1⃣")
st.page_link("pages/streamlit_sample2.py", label="sample 2",icon="2⃣")
st.page_link("pages/requestForm.py", label="依頼書フォーム",icon="🌟")
st.page_link("pages/requestData.py", label="依頼一覧",icon="🌟")

## ユーザー設定読み込み
yaml_path = "conf/config.yaml"

with open(yaml_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    credentials=config['credentials'],
    cookie_name=config['cookie']['name'],
    cookie_key=config['cookie']['key'],
    cookie_expiry_days=config['cookie']['expiry_days'],
)

## UI 
authenticator.login()
if st.session_state["authentication_status"]:
    ## ログイン成功
    with st.sidebar:
        st.markdown(f'## Welcome *{st.session_state["name"]}*')
        authenticator.logout('Logout', 'sidebar')
        st.divider()
    st.write('# ログインしました!')

elif st.session_state["authentication_status"] is False:
    ## ログイン成功ログイン失敗
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    ## デフォルト
    st.warning('Please enter your username and password')