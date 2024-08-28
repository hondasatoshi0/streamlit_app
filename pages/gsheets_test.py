import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Google Sheets APIにアクセスするための認証情報を設定
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("conf/client.json", scope)
client = gspread.authorize(creds)

# スプレッドシートにアクセス
spreadsheet = client.open("Streamlitテスト用")  # スプレッドシートの名前を指定
worksheet = spreadsheet.get_worksheet(0)  # 最初のワークシートを取得

# データを取得してDataFrameに変換
data = worksheet.get_all_records()
df = pd.DataFrame(data)

# Streamlitでデータを表示
st.write(df)
