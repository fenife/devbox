
import streamlit as st
from engine.db import DBClient
from engine.http import HttpClient
from config import Config

st.set_page_config(layout="wide")

if "datas" not in st.session_state:
    st.session_state.datas = []

class Yonder(object):
    def __init__(self) -> None:
        self.db = DBClient(Config.db_conn_str())
        self.http = HttpClient(Config.yonder.host, Config.yonder.port)
    
    def get_category_list(self):
        sql = "select * from categories"
        df = self.db.st_query(sql)    
        st.session_state.datas.append(df)

    def create_category(self, name):
        url = "/api/v1/category"
        body = {"name": name}
        resp = self.http.post(url, body=body)
        with st.container(border=True):
            st.write("response:")
            st.json(resp.json())
        # st.rerun()
 

yonder = Yonder()

with st.sidebar:
    st.markdown("# Yonder page")
                
    clear = st.button("clear datas")
    if clear:
        st.session_state.datas = []

col1, col2 = st.columns([1, 2], gap="small")

@st.dialog("Create Category")
def create_category():
    with st.form("cate_form"):
        cate_name = st.text_input(label="category name")
        submitted = st.form_submit_button("Submit")
        if submitted:
            yonder.create_category(cate_name)


with col1:
    st.button("get category list", on_click=yonder.get_category_list)
    st.button("add category", on_click=create_category)


with col2:
    c1 = st.container(height=700)
    for df in reversed(st.session_state.datas):
        c1.dataframe(df, width=750)