import streamlit as st
import pandas as pd

# ページタイトルとページアイコン
st.title("Streamlit テストページ")

# アップローダー
uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

st.markdown('### 内容表記')

# ファイル読み込み
if uploaded_file:
  df = pd.read_csv(uploaded_file)
  st.write(df.head(5))

# 列選択のためのウィジェット
usecols = st.multiselect(
  '何番目の列を解析の対象にしますか？',
  [0, 3, 4, 5, 6],
  [0, 3, 4, 5, 6]
)

# エラーメッセージ表示
if len(usecols) == 0 or len(names) == 0:
  st.error('解析対象の列が指定されていません。')

# ヘルプテキスト
help_txt = '''
        以下のフォーマット文字列を解析可能です。詳細については、[公式ページ](https://httpd.apache.org/docs/2.4/ja/mod/mod_log_config.html)を参照して下さい。

        | 列名 | フォーマット文字列 | 説明 | 
        |:-----|:-----:|:-----|
        | Remote Host | `%h` | リモートホスト |
        | Time | `%t` | リクエストを受付けた時刻 | 
        | Request | `\"%r\"` | リクエストの最初の行 | 
        | Status | `%>s` | ステータス | 
        | Size | `%b` | レスポンスのバイト数 | 
        | User Agent | `\"%{User-agent}i\"` | リクエストのUser-agentヘッダの内容 | 
        | Response Time | `%D` または `%T` | リクエストを処理するのにかかった時間 |         
        '''

names = st.multiselect(
        'これらの列を何を意味しますか？',
        ['Remote Host', 'Time', 'Request', 'Status', 'Size', 'User Agent', 'Response Time'],
        default_names, help=help_txt)
