import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect
import pandas as pd
# Create a connection object.
credentials = service_account.Credentials.from_service_account_file( '***.json', scopes=[ "https://www.googleapis.com/auth/spreadsheets", ],
)
conn = connect(credentials=credentials)
def run_query(query): rows = conn.execute(query, headers=1) return rows
sheet_url = "https://docs.google.com/spreadsheets/d/15-5s3LOdSheVRPsrhhfeYdfC-QLi7TQVXhYdwbSu-oc/edit?usp=sharing"
rows = run_query(f'SELECT * FROM "{sheet_url}"')
# データフレームに変換し表示する
row_list = []
for row in rows: row_list.append(row)
df=pd.DataFrame(row_list)
st.table(df)
