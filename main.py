import streamlit as st
import pandas as pd

import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.markdown("""
    <style>
    [data-testid="stSidebarNav"] ul {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 初期化
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

if 'password' not in st.session_state:
    st.session_state.password = ""

# ログインフォーム
def show_login_form():
    st.session_state.user_name = st.text_input("ユーザー名")
    st.session_state.password = st.text_input("パスワード", type="password")
    if st.button('ログイン'):
        # 簡易的な認証処理
        if st.session_state.user_name == "admin" and st.session_state.password == "password":
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("ユーザー名またはパスワードが間違っています。")

# ログインしていない場合はログインフォームを表示
if not st.session_state['authenticated']:
    show_login_form()

else:
    # ページタイトルとページアイコン
    st.title("Streamlit main")

    # ページリンク
    st.write("### 依頼書")
    st.page_link("pages/requestForm.py", label="依頼書フォーム",icon="🌟")
    st.page_link("pages/requestData.py", label="依頼一覧",icon="🌟")

    st.write("### サンプル")
    st.page_link("pages/streamlit_sample.py", label="サンプル１",icon="1⃣")
    st.page_link("pages/streamlit_sample2.py", label="サンプル２",icon="2⃣")

    with st.sidebar:
        st.text(f"Username:{st.session_state.user_name}")

    if st.sidebar.button("ログアウト"):
        st.session_state['authenticated'] = False
