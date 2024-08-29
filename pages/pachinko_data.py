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
        # サイドバー設定
        st.sidebar.page_link("main.py", label="ホーム",icon="🏠")

        #! メイン
        st.title("パチンコ成績表")

        st.write('### フィルター機能')
        # 区分リスト取得
        spec_list = [319,349]

        spec_select = st.multiselect(
            '区分を選択',
            spec_list,
            spec_list
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
        spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1-OglKG0sRbalnXCKcFpCUmFBAM6yEM6tnMklZ8QxIQg/edit?usp=sharing")  # スプレッドシートの名前を指定
        worksheet = spreadsheet.get_worksheet(0)  # 最初のワークシートを取得

        # データを取得してDataFrameに変換
        data = worksheet.get_all_records()
        df = pd.DataFrame(data)
        st.write(df)
        # 抽出実行
        data_filter = list(filter(lambda x : x["スペック"] in spec_select, data))

        df = pd.DataFrame(data_filter)

        # Streamlitでデータを表示
        st.write("### パチンコ成績表")
        st.write(df)

except KeyError:
    st.page_link("main.py",label="ログインページへ",icon="🏠")