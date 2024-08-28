import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import configparser

st.title("依頼一覧")

# 設定情報取得
config = configparser.ConfigParser()
config.read('conf/settings.ini')
section_list = []
for i in range(100):
    section_list.append(config["section_list"][f"section_{i}"])

st.write("section_list")

st.write('# ソート機能')
section_select = st.multiselect(
    '所属部署を選択',
    ["製造１課","製造２課","製造３課","エンジニアリング課","押出課","その他"],
    ["製造１課","製造２課","製造３課","エンジニアリング課","押出課","その他"]
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

st.write(data)

# 抽出実行「所属部署」
data_filter = list(filter(lambda x : x["所属部署"] in section_select, data))

df = pd.DataFrame(data_filter)
# Streamlitでデータを表示
st.write(df)
