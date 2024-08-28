import streamlit as st
import datetime
import time
import pyodbc
import re

#
# 全データ項目
all_data_name = [
    'タイムスタンプ',
    '所属部署',
    '依頼者名',
    '依頼内容',
    '写真',
    '製品の品質に関する注意事項内容又は要望',
    '動作に関する注意事項又は要望',
    'そのほかの注意事項内容又は要望',
    '希望納期',
    '緊急性',
    '担当者',
    '進捗ステータス',
    '製作費用',
    '納品完了日時',
    'メモ',
    '納品予定日',
    '納品後回答待ちへ変更した日時',
    '催促メール送信回数',
    '催促メール送信日時1',
    '催促メール送信日時2',
    '納品後回答待ちへ変更'
    ]


class SQLServer:
    def __init__(self):
        # 接続設定
        self.server = ""
        self.username = ""
        self.password = ""
        self.dbname = ""

    def connect(self):
        self.conn_str = "DRIVER={SQL Server};SERVER=" + self.server + \
            ";uid=" + self.username + \
            ";pwd=" + self.password + \
            ";DATABASE=" + self.dbname

        # 接続開始
        self.conn = pyodbc.connect(self.conn_str)
        print("接続成功")
        self.cursor = self.conn.cursor()

    def read(self,table_name,select_name):
        read_data = self.cursor.execute(f"SELECT {select_name} FROM {table_name}").fetchall()
        return read_data

    def insert(self,insert_data,read_data):
        table_name = "T_依頼書一覧"
        for row in insert_data:
            insert_on = True # 追加スイッチ
            data = ["" for _ in range(len(all_data_name))]
            for i in range(len(row)):
                data[i] = row[i]

            # 元データが空の場合
            if len(read_data) == 0:
                # 追加SQL
                self.cursor.execute(f"INSERT INTO {table_name} VALUES {tuple(data)}")
                # 確定
                self.cursor.commit()
            # 読込データが存在する場合、
            else:
                for i in range(len(read_data)):
                    t1 = re.split("[/ :]",row[0])
                    t2 = datetime.datetime(int(t1[0]),int(t1[1]),int(t1[2]),int(t1[3]),int(t1[4]),int(t1[5]))
                    if t2 == read_data[i][0] \
                        and row[3] == str(read_data[i][3]):
                        insert_on = False
                        pass

                if insert_on:
                    # 追加SQL
                    try:
                        self.cursor.execute(f"INSERT INTO {table_name} VALUES {tuple(data)}")
                        # 確定
                        self.cursor.commit()
                    except Exception as e:
                        st.write(f"{e}")

    def updateRequestForm(self,update_data):
        """「T_依頼書一覧」の「担当者」「進捗ステータス」「製作費用」「納品完了日時」「メモ 」「納品予定日」を更新

        Args:
            update_data : [タイムスタンプ,依頼内容,担当者,進捗ステータス,製作費用,納品完了日時,メモ,納品予定日]
        """
        table_name = 'T_依頼書一覧'
        sql_query = f"UPDATE {table_name} SET 担当者 = ?, 進捗ステータス = ?, 製作費用 = ?, 納品完了日時 = ?, メモ = ? ,納品予定日 = ? WHERE タイムスタンプ = ? AND 依頼内容 = ?"
        self.cursor.execute(sql_query, (update_data[2], update_data[3],update_data[4],update_data[5],update_data[6],update_data[7], update_data[0], update_data[1]))
        self.cursor.commit()

    def updateRequestForm2(self,update_data):
        """ 「T_依頼書一覧」の「納品後回答待ちへ変更した日時」,「納品後回答待ちへ変更」を更新

        Args:
            update_data : [タイムスタンプ,依頼内容,納品後回答待ちへ変更した日時,納品後回答待ちへ変更]
        """
        table_name = 'T_依頼書一覧'
        sql_query = f"UPDATE {table_name} SET 納品後回答待ちへ変更した日時 = ? , 納品後回答待ちへ変更 = ? WHERE タイムスタンプ = ? AND 依頼内容 = ?"
        self.cursor.execute(sql_query, (update_data[2],update_data[3],update_data[0], update_data[1]))
        self.cursor.commit()

    def updateRequestForm_remind1(self,update_data):
        """ 「T_依頼書一覧」の「催促メール送信回数」,「催促メール送信日時1」を更新

        Args:
            update_data : [タイムスタンプ,依頼内容,催促メール送信回数,催促メール送信日時1]
        """
        table_name = 'T_依頼書一覧'
        sql_query = f"UPDATE {table_name} SET 催促メール送信回数 = ? , 催促メール送信日時1 = ? WHERE タイムスタンプ = ? AND 依頼内容 = ?"
        self.cursor.execute(sql_query, (update_data[2],update_data[3],update_data[0], update_data[1]))
        self.cursor.commit()

    def updateRequestForm_remind2(self,update_data):
        """ 「T_依頼書一覧」の「催促メール送信回数」,「催促メール送信日時2」を更新

        Args:
            update_data : [タイムスタンプ,依頼内容,催促メール送信回数,催促メール送信日時2]
        """
        table_name = 'T_依頼書一覧'
        sql_query = f"UPDATE {table_name} SET 催促メール送信回数 = ? , 催促メール送信日時2 = ? WHERE タイムスタンプ = ? AND 依頼内容 = ?"
        self.cursor.execute(sql_query, (update_data[2],update_data[3],update_data[0], update_data[1]))
        self.cursor.commit()

    def insertHistory(self,insert_data):
        table_name = "T_依頼書履歴"
        # 追加SQL
        self.cursor.execute(f"INSERT INTO {table_name} VALUES {tuple(insert_data)}")
        # 確定
        self.cursor.commit()

    def close(self):
        # 接続を切る
        self.cursor.close()
        self.conn.close()


#!初回動作

# 設定
S = SQLServer()
S.server = '192.168.1.5\SQLEXPRESS'
S.username = 'sa'
S.password = 'taiyo3553'
S.dbname = 'IoTtest'

# 接続
S.connect()
# 読込
Pic_list = S.read(table_name='T_設備機械課員',select_name='番号,氏名,メールアドレス,役職,パスワード,編集権限,更新権限,閲覧権限,出力権限') # 設備機械課員読込
ProgressStatus_list = S.read(table_name='T_進捗ステータス',select_name='番号,ステータス') # 進捗ステータス読込
department_list = S.read(table_name='T_課一覧',select_name='番号,課,所属長氏名,所属長連絡先') # 課一覧読込
file_version_list = S.read(table_name='T_バージョン管理',select_name='ファイル名,バージョン') # ファイルバージョン読込

st.write(Pic_list)

# 初期値設定
if 'section' not in st.session_state:
    st.session_state.section = ''

if 'name' not in st.session_state:
    st.session_state.name = ''

if 'request' not in st.session_state:
    st.session_state.request = ''

if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = ''
    
if 'request_detail1' not in st.session_state:
    st.session_state.request_detail1 = ''

if 'request_detail2' not in st.session_state:
    st.session_state.request_detail2 = ''

if 'request_detail3' not in st.session_state:
    st.session_state.request_detail3 = ''

if 'd' not in st.session_state:
    st.session_state.d = ''

if 'check' not in st.session_state:
    st.session_state.check = ''

# セッションステートで現在のページを管理
if 'page' not in st.session_state:
    st.session_state.page = 'page1'

# ページ移行の関数
def go_to_page(page_name):
    st.session_state.page = page_name

# ページごとのコンテンツを表示
if st.session_state.page == 'page1':
    st.title("依頼書フォーム")

    # 注釈
    st.caption("*必須の質問")
    
    # 部署
    st.session_state.section = st.selectbox("所属部署*", ["製造１課","製造２課","製造３課","エンジニアリング部","押出課","その他"], index = None, placeholder = "所属部署を選択してください。")
    
    # 氏名
    name = st.text_input("氏名*")
    st.session_state.name = name.replace(' ','').replace('　','')
    
    # 依頼内容
    st.session_state.request = st.text_input("依頼内容（最大200文字）*", max_chars = 200)
    
    # ファイルアップロード
    st.session_state.uploaded_file = st.file_uploader("写真や資料があればこちらからアップロードしてください。（１つまで）")
    
    # 依頼詳細１
    st.session_state.request_detail1 = st.text_input("製品の品質に関する注意事項内容又は要望（最大200文字）", max_chars = 200)
    
    # 依頼詳細２
    st.session_state.request_detail2 = st.text_input("動作に関する注意事項又は要望（最大200文字）", max_chars = 200)
    
    # 依頼詳細３
    st.session_state.request_detail3 = st.text_input("そのほかの注意事項内容又は要望（最大200文字）", max_chars = 200)
    
    # 希望納期
    st.session_state.d = st.date_input("希望納期*", value = None)
    
    # 緊急性
    st.write("緊急ですか？")
    st.session_state.check = st.checkbox("はい")
    
    # 送信ボタン
    if st.button("送信"):
        if st.session_state.section is not None \
            and st.session_state.name is not None and not st.session_state.name == "" \
                and st.session_state.request is not None and not st.session_state.request == "" \
                    and st.session_state.d is not None:
            go_to_page('page2')
            st.rerun()
        else:
            if st.session_state.section is None:
                st.error("【エラー】所属部署を選択してください。")
            if st.session_state.name is None or st.session_state.name == "":
                st.error("【エラー】氏名を入力してください。")
            if st.session_state.request is None or st.session_state.request == "":
                st.error("【エラー】依頼内容を入力してください。")
            if st.session_state.d is None:
                st.error("【エラー】希望納期を選択してください。")

elif st.session_state.page == 'page2':
    st.title("回答を送信しました。")
    st.write(f"所属部署：{st.session_state.section}")
    st.write(f"氏名：{st.session_state.name}")
    st.write(f"依頼内容：{st.session_state.request}")
    st.write(f"ファイル：{st.session_state.uploaded_file}")
    st.write(f"製品の品質に関する注意事項内容又は要望：{st.session_state.request_detail1}")
    st.write(f"動作に関する注意事項又は要望：{st.session_state.request_detail2}")
    st.write(f"そのほかの注意事項内容又は要望：{st.session_state.request_detail3}")
    st.write(f"希望納期：{st.session_state.d}")
    st.write(f"緊急性：{st.session_state.check}")
    
    if st.button("別の回答を送信"):
        go_to_page('page1')
        st.rerun()



