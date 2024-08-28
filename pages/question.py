import streamlit as st
import datetime
import time
import pytz
import re

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


# 初期値設定
if 'section' not in st.session_state:
    st.session_state.section = ''

if 'name' not in st.session_state:
    st.session_state.name = ''

if 'request' not in st.session_state:
    st.session_state.request = ''

if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = ''

if 'request_detail1' not in st.session_state:
    st.session_state.request_detail1 = ''

if 'request_detail2' not in st.session_state:
    st.session_state.request_detail2 = ''

if 'request_detail3' not in st.session_state:
    st.session_state.request_detail3 = ''

if 'd' not in st.session_state:
    st.session_state.d = ''

if 'check' not in st.session_state:
    st.session_state.check = ''

# セッションステートで現在のページを管理
if 'page' not in st.session_state:
    st.session_state.page = 'page1'

# ページ移行の関数
def go_to_page(page_name):
    st.session_state.page = page_name

# ページごとのコンテンツを表示
if st.session_state.page == 'page1':
    cols = st.columns(2)
    with cols[0]:
      st.title("依頼書フォーム")
    with cols[1]:
      st.write(f"現在日時：{datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%Y/%m/%d %H:%M:%S")}")

    # 注釈
    st.caption("*必須の質問")

    # 部署
    st.session_state.section = st.selectbox("所属部署*", ["製造１課","製造２課","製造３課","エンジニアリング部","押出課","その他"], index = None, placeholder = "所属部署を選択してください。")
    
    # 氏名
    name = st.text_input("氏名*")
    st.session_state.name = name.replace(' ','').replace('　','')
    
    # 依頼内容
    st.session_state.request = st.text_input("依頼内容（最大200文字）*", max_chars = 200)
    
    # ファイルアップロード
    st.session_state.uploaded_file = st.file_uploader("写真や資料があればこちらからアップロードしてください。（１つまで）")
    
    # 依頼詳細１
    st.session_state.request_detail1 = st.text_input("製品の品質に関する注意事項内容又は要望（最大200文字）", max_chars = 200)
    
    # 依頼詳細２
    st.session_state.request_detail2 = st.text_input("動作に関する注意事項又は要望（最大200文字）", max_chars = 200)
    
    # 依頼詳細３
    st.session_state.request_detail3 = st.text_input("そのほかの注意事項内容又は要望（最大200文字）", max_chars = 200)
    
    # 希望納期
    st.session_state.d = st.date_input("希望納期*", value = None)
    
    # 緊急性
    st.write("緊急ですか？")
    st.session_state.check = st.checkbox("はい")
    
    # 送信ボタン
    if st.button("送信"):
        if st.session_state.section is not None \
            and st.session_state.name is not None and not st.session_state.name == "" \
                and st.session_state.request is not None and not st.session_state.request == "" \
                    and st.session_state.d is not None:
            go_to_page('page2')
            st.rerun()
        else:
            if st.session_state.section is None:
                st.error("【エラー】所属部署を選択してください。")
            if st.session_state.name is None or st.session_state.name == "":
                st.error("【エラー】氏名を入力してください。")
            if st.session_state.request is None or st.session_state.request == "":
                st.error("【エラー】依頼内容を入力してください。")
            if st.session_state.d is None:
                st.error("【エラー】希望納期を選択してください。")

elif st.session_state.page == 'page2':
    st.title("回答を送信しました。")
    
    # 認証情報
    credentials = {
        "type": st.secrets["gcp_service_account"]["type"],
        "project_id": st.secrets["gcp_service_account"]["project_id"],
        "private_key_id": st.secrets["gcp_service_account"]["private_key_id"],
        "private_key": st.secrets["gcp_service_account"]["private_key"],
        "client_email": st.secrets["gcp_service_account"]["client_email"],
        "client_id": st.secrets["gcp_service_account"]["client_id"],
        "auth_uri": st.secrets["gcp_service_account"]["auth_uri"],
        "token_uri": st.secrets["gcp_service_account"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["gcp_service_account"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["gcp_service_account"]["client_x509_cert_url"]
    }
    
    # 認証情報を使用してGoogle Sheets APIにアクセス
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials, scope)
    client = gspread.authorize(creds)
    
    # スプレッドシートにアクセス
    spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/15-5s3LOdSheVRPsrhhfeYdfC-QLi7TQVXhYdwbSu-oc/edit?usp=sharing")  # スプレッドシートのURL
    worksheet = spreadsheet.get_worksheet(0)  # 最初のワークシートを取得
    
    # データを取得してDataFrameに変換
    # data = worksheet.get_all_records()
    # df = pd.DataFrame(data)
    
    # Streamlitでデータを表示
    # st.write(df)
    
    # データを書き込む
    new_data = [datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%Y/%m/%d %H:%M:%S"),
                st.session_state.section,
                st.session_state.name,
                st.session_state.request_detail1,
                st.session_state.request_detail2,
                st.session_state.request_detail3,
                st.session_state.d,
                st.session_state.check
    ]

        # データがリスト形式であることを確認
    if isinstance(new_data, list):
        worksheet.append_row(new_data)
    else:
        st.error("追加するデータはリスト形式でなければなりません。")
    
    st.write("データがスプレッドシートに書き込まれました。")

    st.write(f"依頼日時：{datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%Y/%m/%d %H:%M:%S")}")
    st.write(f"所属部署：{st.session_state.section}")
    st.write(f"氏名：{st.session_state.name}")
    st.write(f"依頼内容：{st.session_state.request}")
    st.write(f"ファイル：{st.session_state.uploaded_file}")
    st.write(f"製品の品質に関する注意事項内容又は要望：{st.session_state.request_detail1}")
    st.write(f"動作に関する注意事項又は要望：{st.session_state.request_detail2}")
    st.write(f"そのほかの注意事項内容又は要望：{st.session_state.request_detail3}")
    st.write(f"希望納期：{st.session_state.d}")
    st.write(f"緊急性：{st.session_state.check}")
    
    if st.button("別の回答を送信"):
        go_to_page('page1')
        st.rerun()



