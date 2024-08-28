import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

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
df = pd.DataFrame(data)

# Streamlitでデータを表示
st.write(df)
