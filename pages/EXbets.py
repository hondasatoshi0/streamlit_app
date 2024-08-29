import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import configparser
import datetime
import pytz
import time

# サイドバーにページリンクを非表示
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] ul {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 初期値設定
if 'date' not in st.session_state:
    st.session_state.date = ''

if 'investment' not in st.session_state:
    st.session_state.investment = 0

if 'payback' not in st.session_state:
    st.session_state.payback = 0

if 'diff' not in st.session_state:
    st.session_state.diff = 0

if 'category' not in st.session_state:
    st.session_state.category = ''

if 'model_name' not in st.session_state:
    st.session_state.model_name = ''

if 'memo' not in st.session_state:
    st.session_state.memo = ''

if 'firstLoop' not in st.session_state:
    st.session_state.firstLoop = True


# ページ移行の関数
if 'page' not in st.session_state:
    st.session_state.page = "page1"
def go_to_page(page_name):
    st.session_state.page = page_name

try:
    if not st.session_state['authenticated']:
        st.page_link("main.py",label="ログインページへ",icon="🏠")
    else:
        if not st.session_state['user_name'] == 'satoshi_honda':
            st.write("アクセス権限がありません。")
            st.page_link("main.py",label="ホームへ",icon="🏠")
        else:
            # サイドバー設定
            st.sidebar.page_link("main.py", label="ホーム",icon="🏠")

            #! メイン
            st.title("ギャンブル収支")

            # カテゴリーリスト設定
            category_list = ["麻雀","パチンコ","スロット"]

            if st.session_state.page == 'page1':
                if st.session_state.firstLoop:
                    # フィルター
                    st.write('### フィルター機能')
                    category_select = st.multiselect(
                        'カテゴリーを選択',
                        category_list,
                        category_list
                    )

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
                    spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1r-g-Khzwjcc-SS0CRtXWj5Ljx4u3YAfRRUR-LjRtwbA/edit?usp=sharing")  # スプレッドシートの名前を指定
                    worksheet = spreadsheet.get_worksheet(0)  # 最初のワークシートを取得

                    # データを取得してDataFrameに変換
                    data = worksheet.get_all_records()

                    # 抽出実行「所属部署」
                    data_filter = list(filter(lambda x : x["カテゴリー"] in category_select, data))

                    df = pd.DataFrame(data_filter)

                    # Streamlitでデータを表示
                    st.write("### ギャンブル収支表")
                    st.write(df)

                    st.session_state.firstLoop = False

                st.markdown("---") # 区切り線

                #! 入力
                st.write("## 入力")
                # 日付
                st.session_state.date = st.date_input("日時", value = datetime.datetime.now(pytz.timezone('Asia/Tokyo')), format ="YYYY/MM/DD")
                # 金額入力
                cols = st.columns(3)
                with cols[0]:
                    # 投資金額
                    st.session_state.investment = st.number_input("投資金額",step=500)
                with cols[1]:
                    # 回収金額
                    st.session_state.payback = st.number_input("回収金額",step=500)
                with cols[2]:
                    # 差額
                    st.write("差額")
                    st.session_state.diff = int(st.session_state.payback) - (st.session_state.investment)
                    st.write(st.session_state.diff)

                cols2 = st.columns(2)
                with cols2[0]:
                    # カテゴリー
                    st.session_state.category = st.selectbox("カテゴリー", category_list, index = None, placeholder = "カテゴリーを選択してください。")
                with cols2[1]:
                    # 機種名
                    st.session_state.model_name = st.text_input("機種")

                # メモ
                st.session_state.memo = st.text_input("メモ")

                if st.button("登録"):
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
                    spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1r-g-Khzwjcc-SS0CRtXWj5Ljx4u3YAfRRUR-LjRtwbA/edit?usp=sharing")  # スプレッドシートの名前を指定
                    worksheet = spreadsheet.get_worksheet(0)  # 最初のワークシートを取得

                    # データ登録
                    new_data = [st.session_state.date.strftime("%Y/%m/%d"),
                                int(st.session_state.investment),
                                int(st.session_state.payback),
                                int(st.session_state.diff),
                                st.session_state.category,
                                st.session_state.model_name,
                                st.session_state.memo
                    ]

                    # データ登録
                    worksheet.append_row(new_data)
                    go_to_page('page2')
                    st.rerun()

            elif st.session_state.page == 'page2':
                st.success("登録完了")

                if st.button("戻る"):
                    go_to_page('page1')
                    st.rerun()

except KeyError:
    st.page_link("main.py",label="ログインページへ",icon="🏠")