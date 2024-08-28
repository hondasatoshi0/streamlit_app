import streamlit as st
from gsheetsdb import connect
import pandas as pd

conn = connect()
def run_query(query):
  rows = conn.execute(query, headers=1)
  return rows

sheet_url = "https://docs.google.com/spreadsheets/d/15-5s3LOdSheVRPsrhhfeYdfC-QLi7TQVXhYdwbSu-oc/edit?usp=sharing"

rows = run_query(f'SELECT * FROM "{sheet_url}"')

st.write("スプレッドシート内容表示")
row_list = []
for row in rows:
  row_list.append(row)
  df=pd.DataFrame(row_list)
  st.table(df)
