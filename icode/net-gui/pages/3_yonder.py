
import datetime
import streamlit as st
from engine.db import DBClient
from engine.http import HttpClient
from config import Config


class Yonder(object):
    def __init__(self) -> None:
        self.db = DBClient(Config.db_conn_str())
        self.http = HttpClient(Config.yonder.host, Config.yonder.port)

    # @st.cache_data(ttl=60)
    def get_user_list(self):
        sql = "select * from users"
        df = self.db.st_query(sql)
        return df, sql

    def get_users(self):
        df, _ = self.get_user_list()
        users = list(zip(df['id'], df['name']))
        return users

    def create_user(self, name, passwd):
        url = "/api/v1/user/signup"
        body = {"name": name, "password": passwd}
        resp = self.http.post(url, body=body)
        return resp

    # @st.cache_data(ttl=60)
    def get_category_list(self):
        sql = "select * from categories"
        df = self.db.st_query(sql)
        return df, sql

    def get_cates(self):
        df, _ = self.get_category_list()
        cates = list(zip(df['id'], df['name']))
        return cates

    def create_category(self, name):
        url = "/api/v1/category"
        body = {"name": name}
        resp = self.http.post(url, body=body)
        return resp

    def get_post_list(self):
        sql = "select * from posts"
        df = self.db.st_query(sql)
        return df, sql

    def create_category(self, title, content, user_id, cate_id):
        url = "/api/v1/post"
        body = {"title": title,
                "content": content,
                "cate_id": cate_id,
                "user_id": user_id}
        resp = self.http.post(url, body=body)
        return resp


yonder = Yonder()

############################################################
# layout

st.set_page_config(layout="wide")

if "datas" not in st.session_state:
    st.session_state.datas = []
if "user" not in st.session_state:
    st.session_state.user = {}
if "cate" not in st.session_state:
    st.session_state.cate = {}
if "post" not in st.session_state:
    st.session_state.post = {}

col1, col2 = st.columns([1, 2], gap="small")
# c2 = col2.container(height=700)

with st.sidebar:
    st.markdown("# Yonder page")

    if st.button("clear datas"):
        st.session_state.datas = []
        st.session_state.user = {}
        st.session_state.cate = {}
        st.session_state.post = {}

############################################################
# view

class Viewer(object):
    def __init__(self) -> None:
        super().__init__()

    def show_user_list(self):
        df, sql = yonder.get_user_list()
        # with col2.container(border=True):
        #     st.write(datetime.datetime.now(), sql)
        #     st.dataframe(df, width=750)
        st.session_state.user = {
            "ts": datetime.datetime.now(),
            "sql": sql,
            "df": df
        }

    @st.dialog("Create User")
    def create_user(self):
        with st.form("user_form"):
            username = st.text_input(label="username")
            passwd = st.text_input(label="password")
            submitted = st.form_submit_button("Submit")
            if submitted:
                resp = yonder.create_user(username, passwd)
                with st.container(border=True):
                    st.write("response:")
                    st.json(resp.json())

    def show_category_list(self):
        df, sql = yonder.get_category_list()
        # st.session_state.datas.append(df)
        # with col2.container(border=True):
        #     st.write(datetime.datetime.now(), sql)
        #     st.dataframe(df, width=750)
        st.session_state.cate = {
            "ts": datetime.datetime.now(),
            "sql": sql,
            "df": df
        }

    @st.dialog("Create Category")
    def create_category(self):
        with st.form("cate_form"):
            cate_name = st.text_input(label="category name")
            submitted = st.form_submit_button("Submit")
            if submitted:
                resp = yonder.create_category(cate_name)
                with st.container(border=True):
                    st.write("response:")
                    st.json(resp.json())

    def show_post_list(self):
        df, sql = yonder.get_post_list()
        # with col2.container(border=True):
        #     st.write(datetime.datetime.now(), sql)
        #     st.dataframe(df, width=750)
        st.session_state.post = {
            "ts": datetime.datetime.now(),
            "sql": sql,
            "df": df
        }

    @st.dialog("Create Post")
    def create_post(self):
        with st.form("post_form"):
            title = st.text_input(label="title")
            user = st.selectbox(label="user", options=yonder.get_users())
            cate = st.selectbox(label="category", options=yonder.get_cates())
            content = st.text_area(label="content")
            submitted = st.form_submit_button("Submit")
            if submitted:
                post = {"title": title,
                        "content": content,
                        "user_id": user[0],
                        "cate_id": cate[0]}
                st.write("post:")
                st.json(post)
                # resp = yonder.create_post(title, content, 0, 0)
                # with st.container(border=True):
                #     st.write("response:")
                #     st.json(resp.json())


viewer = Viewer()

#------------------------------------------------------------ 
# col1

with col1.container(border=True):
    st.markdown("##### user")
    if st.button("all user (db)"):
        viewer.show_user_list()

    if st.button("add user (http)"):
        viewer.create_user()

with col1.container(border=True):
    st.markdown("##### category")
    if st.button("all category (db)"):
        viewer.show_category_list()

    if st.button("add category (http)"):
        viewer.create_category()

with col1.container(border=True):
    st.markdown("##### post")
    if st.button("all post (db)"):
        viewer.show_post_list()

    if st.button("add post (http)"):
        viewer.create_post()

#------------------------------------------------------------ 
# col2

with col2.container(border=True):
    user = st.session_state.user
    if user:
        st.write(user["ts"], user["sql"])
        st.dataframe(user["df"], width=750)

with col2.container(border=True):
    cate = st.session_state.cate
    if cate:
        st.write(cate["ts"], cate["sql"])
        st.dataframe(cate["df"], width=750, height=250)

with col2.container(border=True):
    data = st.session_state.post
    if data:
        st.write(data["ts"], data["sql"])
        st.dataframe(data["df"], width=750)

# with col2:
#     c1 = st.container(height=700)
#     for df in reversed(st.session_state.datas):
#         c1.dataframe(df, width=750)
