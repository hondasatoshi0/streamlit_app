import streamlit as st
import pandas as pd

### 表示系 
# テキスト（マークダウンで書ける）
st.write("# tilte")

# 注釈
st.caption("注釈")

# 画像
st.image("サンプル.png")

# テーブル
df = pd.DataFrame(
  {
    "first colum": [1,2,3,4],
    "second column":[10,20,30,40],
  }
)
st.write(df)

# チャート
st.line_chart(df)

### ユーザー入力系
# テキスト入力
name = st.text_input("名前")

# 数値入力
age = st.number_input("年齢",step = 1)

st.write(f"名前:{name}")
st.write(f"年齢:{age}")

# ボタン
if st.button("Push"):
  st.write("Button pushed.")

# プルダウン
select = st.selectbox("好きな役",["一発","立直","槍槓"])
st.write(select)

# プルダウン（複数選択）
multi_select = st.multiselect("好きな雀士",["多井","瀬戸熊","堀内","堀"])
if multi_select is not None:
  for i in range(len(multi_select)):
    st.write(multi_select[i])

# チェックボックス
check = st.checkbox("OK")
st.write(f"チェック:{check}")

# ラジオボタン
radio = st.radio("選択",["猫","犬"])
st.write(f"ラジオ:{radio}")

# ファイルアップロード
uploaded_file = st.file_uploader("upload",type=["csv"])
if uploaded_file:
  df = pd.read_csv(uploaded_file)
  st.write(df)

### レイアウト系
# 横に並べる
cols = st.columns(2)
with cols[0]:
  st.write("列1")
with cols[1]:
  st.write("列2")

# タブ
tabs = st.tabs(["タブ1","タブ2"])
with tabs[0]:
  st.write("タブ1")
with tabs[1]:
  st.write("タブ2")

# ?
st.write("アコーディオン")

# アコーディオン
with st.expander("開きます"):
  st.write("開きました。")

# サイドバー
with st.sidebar:
  st.write("サイドバー内に表示されます")
