import streamlit as st
import datetime
import re

# 初期値設定
if 'section' not in st.session_state:
    st.session_state.section = ''

if 'name' not in st.session_state:
    st.session_state.name = ''

if 'request' not in st.session_state:
    st.session_state.request = ''

# セッションステートで現在のページを管理
if 'page' not in st.session_state:
    st.session_state.page = 'page1'

# ページ移行の関数
def go_to_page(page_name):
    st.session_state.page = page_name

# ページごとのコンテンツを表示
if st.session_state.page == 'page1':
    st.title("依頼書フォーム")
    
    # 部署
    st.session_state.section = st.selectbox("所属部署", ["製造１課","製造２課","製造３課","エンジニアリング部","押出課","その他"], index = None, placeholder = "所属部署を選択してください。")
    
    # 氏名
    name = st.text_input("氏名")
    st.session_state.name = name.replace(' ','').replace('　','')
    st.write("氏名:",name)
    
    # 依頼内容
    st.session_state.request = st.text_input("依頼内容（最大200文字）　※必須", max_chars = 200)
    
    # ファイルアップロード
    st.write("写真や資料があればこちらからアップロードしてください。（１つまで）")
    uploaded_file = st.file_uploader("アップロード")
    
    # 依頼詳細１
    request_detail1 = st.text_input("製品の品質に関する注意事項内容又は要望（最大200文字）　※必須", max_chars = 200)
    
    # 依頼詳細２
    request_detail2 = st.text_input("動作に関する注意事項又は要望（最大200文字）　※必須", max_chars = 200)
    
    # 依頼詳細３
    request_detail3 = st.text_input("そのほかの注意事項内容又は要望（最大200文字）　※必須", max_chars = 200)
    
    # 希望納期
    d = st.date_input("希望納期　※必須", value = None)
    
    # 緊急性
    st.write("緊急ですか？")
    check = st.checkbox("はい")
    
    # 送信ボタン
    if st.button("送信"):
      go_to_page('page2')

elif st.session_state.page == 'page2':
    st.title("回答を送信しました")
    st.write(f"所属部署：{st.session_state.section}")
    st.write(f"氏名：{st.session_state.name}")
    st.write(f"依頼内容：{st.session_state.request}")
    
    if st.button("別の回答を送信"):
        go_to_page('page1')



