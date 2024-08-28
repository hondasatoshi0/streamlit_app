import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect
import pandas as pd
# Create a connection object.
credentials = service_account.Credentials.from_service_account_info( st.secrets["gcp_service_account"], scopes=[ "https://www.googleapis.com/auth/spreadsheets", ],
)
conn = connect(credentials=credentials)
def run_query(query): rows = conn.execute(query, headers=1) return rows
sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')
# データフレームに変換し表示する
row_list = []
for row in rows: row_list.append(row)
df=pd.DataFrame(row_list)
st.table(df)
