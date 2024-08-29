import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import configparser

# サイドバーにページリンクを非表示
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] ul {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

try:
    if not st.session_state['authenticated']:
        st.page_link("main.py",label="ログインページへ",icon="🏠")
    else:
        #! メイン
        st.title("依頼一覧")

        st.write('### フィルター機能')
        # 部署リスト取得
        config = configparser.ConfigParser()
        config.read('conf/settings.ini')
        section_list = []
        try:
            for i in range(100):
                section_list.append(config["section_list"][f"section_{i}"])
        except KeyError:
            pass

        section_select = st.multiselect(
            '所属部署を選択',
            section_list,
            section_list
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
        spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/15-5s3LOdSheVRPsrhhfeYdfC-QLi7TQVXhYdwbSu-oc/edit?usp=sharing")  # スプレッドシートの名前を指定
        worksheet = spreadsheet.get_worksheet(0)  # 最初のワークシートを取得

        # データを取得してDataFrameに変換
        data = worksheet.get_all_records()

        # 抽出実行「所属部署」
        data_filter = list(filter(lambda x : x["所属部署"] in section_select, data))

        df = pd.DataFrame(data_filter)

        # Streamlitでデータを表示
        st.write("### 依頼一覧表")
        st.write(df)

        # サイドバー設定
        st.sidebar.page_link("main.py", label="ホーム",icon="🏠")

except KeyError:
    st.page_link("main.py",label="ログインページへ",icon="🏠")