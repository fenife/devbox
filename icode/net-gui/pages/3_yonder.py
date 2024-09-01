
import datetime
import streamlit as st
from engine.db import DBClient, DBResult
from engine.http import HttpClient
from config import Config


############################################################
# yonder

class Yonder(object):
    def __init__(self) -> None:
        self.db = DBClient(Config.db_conn_str())
        self.http = HttpClient(Config.yonder.host, Config.yonder.port)

    # @st.cache_data(ttl=60)
    def get_user_list(self):
        sql = "select * from users"
        result = self.db.query(sql)
        return result

    def get_users(self):
        result = self.get_user_list()
        df = result.df
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
        result = self.db.query(sql)
        return result

    def get_cates(self):
        result = self.get_category_list()
        df = result.df
        cates = list(zip(df['id'], df['name']))
        return cates

    def create_category(self, name):
        url = "/api/v1/category"
        body = {"name": name}
        resp = self.http.post(url, body=body)
        return resp

    def get_post_list(self):
        sql = "select * from posts"
        result =self.db.query(sql)
        return result

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
    st.session_state.user = None
if "cate" not in st.session_state:
    st.session_state.cate = None
if "post" not in st.session_state:
    st.session_state.post = None

col1, col2 = st.columns([1, 2], gap="small")
# c2 = col2.container(height=700)

with st.sidebar:
    st.markdown("# Yonder page")

    if st.button("clear datas"):
        st.session_state.datas = []
        st.session_state.user = None
        st.session_state.cate = None
        st.session_state.post = None

############################################################
# view

class Viewer(object):
    def __init__(self) -> None:
        super().__init__()

    def show_user_list(self):
        result = yonder.get_user_list()
        st.session_state.user = result
        # with col2.container(border=True):
        #     st.write(datetime.datetime.now(), sql)
        #     st.dataframe(df, width=750)
        # st.session_state.user = {
        #     "ts": datetime.datetime.now(),
        #     "sql": sql,
        #     "df": df
        # }

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
        result = yonder.get_category_list()
        st.session_state.cate = result
        # st.session_state.datas.append(df)
        # with col2.container(border=True):
        #     st.write(datetime.datetime.now(), sql)
        #     st.dataframe(df, width=750)
        # st.session_state.cate = {
        #     "ts": datetime.datetime.now(),
        #     "sql": sql,
        #     "df": df
        # }

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
        result = yonder.get_post_list()
        st.session_state.post = result
        # with col2.container(border=True):
        #     st.write(datetime.datetime.now(), sql)
        #     st.dataframe(df, width=750)
        # st.session_state.post = {
        #     "ts": datetime.datetime.now(),
        #     "sql": sql,
        #     "df": df
        # }

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

    def view_dataframe(self, data: DBResult):
        if data:
            st.write(data.dt, data.sql)
            st.dataframe(data.df, width=750)


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
    viewer.view_dataframe(st.session_state.user)

with col2.container(border=True):
    viewer.view_dataframe(st.session_state.cate)

with col2.container(border=True):
    viewer.view_dataframe(st.session_state.post)

# with col2:
#     c1 = st.container(height=700)
#     for df in reversed(st.session_state.datas):
#         c1.dataframe(df, width=750)
