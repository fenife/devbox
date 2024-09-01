
from collections import namedtuple
import datetime
import json
import streamlit as st
from streamlit.elements.dialog_decorator import F
from engine.db import DBClient, DBResult
from engine.http import HttpClient
from config import Config


############################################################
# yonder

def cache_hash_funcs():
    hash_funcs = {"__main__.Yonder": lambda x: "Yonder"}
    return hash_funcs


class Yonder(object):
    def __init__(self) -> None:
        self.db = DBClient(Config.db_conn_str())
        self.http = HttpClient(Config.yonder.host, Config.yonder.port)

    def cache_clear(self):
        st.cache_data.clear()

    # hash_funcs, key: class type
    @st.cache_data(ttl=10, hash_funcs=cache_hash_funcs())
    def get_user_list(self):
        sql = "select * from users"
        result = self.db.query(sql)
        return result

    def get_select_users(self):
        result = self.get_user_list()
        df = result.df
        users = list(df.itertuples(name='User', index=False))
        return users

    def create_user(self, name, passwd):
        url = "/api/v1/user/signup"
        body = {"name": name, "password": passwd}
        resp = self.http.post(url, body=body)
        self.cache_clear()
        return resp

    @st.cache_data(ttl=10, hash_funcs=cache_hash_funcs())
    def get_category_list(self):
        sql = "select * from categories"
        result = self.db.query(sql)
        return result

    def get_select_cates(self):
        result = self.get_category_list()
        df = result.df
        cates = list(df.itertuples(name='Cate', index=False))
        return cates

    def create_category(self, name):
        url = "/api/v1/category"
        body = {"name": name}
        resp = self.http.post(url, body=body)
        self.cache_clear()
        return resp

    @st.cache_data(ttl=10, hash_funcs=cache_hash_funcs())
    def get_post_list(self):
        sql = "select * from posts"
        result = self.db.query(sql)
        return result

    def create_post(self, title, content, user_id, cate_id):
        url = "/api/v1/post"
        body = {"title": title,
                "content": content,
                "cate_id": cate_id,
                "user_id": user_id}
        resp = self.http.post(url, body=body)
        self.cache_clear()
        return resp


yonder = Yonder()

############################################################
# layout

st.set_page_config(layout="wide")

if "datas" not in st.session_state:
    st.session_state.datas = []

if "users" not in st.session_state:
    st.session_state.users = None
if "cates" not in st.session_state:
    st.session_state.cates = None
if "posts" not in st.session_state:
    st.session_state.posts = None

if "user" not in st.session_state:
    st.session_state.user = None
if "cate" not in st.session_state:
    st.session_state.cate = None
if "post" not in st.session_state:
    st.session_state.post = None

with st.sidebar:
    st.markdown("# Yonder page")

    if st.button("clear datas"):
        st.session_state.datas = []

        st.session_state.users = None
        st.session_state.cates = None
        st.session_state.posts = None

        st.session_state.user = None
        st.session_state.cate = None
        st.session_state.post = None


col1, col2 = st.columns([1, 2], gap="small")
# c2 = col2.container(height=700)


############################################################
# view


def _format_select_label(r: namedtuple):
    s = f"{r.id}-{r.name}"
    return s


class Viewer(object):
    def __init__(self) -> None:
        super().__init__()

    def show_user_list(self):
        result = yonder.get_user_list()
        st.session_state.users = result

    @st.dialog("Create User")
    def create_user(self):
        with st.form("user_form"):
            username = st.text_input(label="username")
            passwd = st.text_input(label="password")
            submitted = st.form_submit_button("Submit")
            if not submitted:
                return 
            resp = yonder.create_user(username, passwd)
            with st.container(border=True):
                st.write("response:")
                st.json(resp.json())

    def show_category_list(self):
        result = yonder.get_category_list()
        st.session_state.cates = result

    @st.dialog("Create Category")
    def create_category(self):
        with st.form("cate_form"):
            cate_name = st.text_input(label="category name")
            submitted = st.form_submit_button("Submit")
            if not submitted:
                return 
            resp = yonder.create_category(cate_name)
            with st.container(border=True):
                st.write("response:")
                st.json(resp.json())

    def show_post_list(self):
        result = yonder.get_post_list()
        st.session_state.posts = result

    @st.dialog("Create Post")
    def create_post(self):
        with st.form("post_form"):
            title = st.text_input(label="title")
            user = st.selectbox(label="user", options=yonder.get_select_users(),
                                format_func=_format_select_label)
            cate = st.selectbox(label="category", options=yonder.get_select_cates(),
                                format_func=_format_select_label)
            content = st.text_area(label="content")
            submitted = st.form_submit_button("Submit")
            if not submitted:
                return 
            post = {"title": title,
                    "content": content,
                    "user_id": user.id,
                    "cate_id": cate.id}
            st.write("post:")
            st.json(post)
            # resp = yonder.create_post(title, content, 0, 0)
            # with st.container(border=True):
            #     st.write("response:")
            #     st.json(resp.json())

    def view_dataframe(self, data: DBResult):
        if data:
            st.write(data.dt, data.sql)
            if len(data.df) < 5:
                st.dataframe(data.df, width=750)
            else:
                st.dataframe(data.df, width=750, height=220)

    def select_cur_cate(self):
        with st.container(border=True):
            cate = st.selectbox(label="category", index=None,
                                options=yonder.get_select_cates(),
                                format_func=_format_select_label)
            if not cate:
                return
            d = dict(zip(cate._fields, map(str, list(cate))))
            # st.text(f"cate: {cate.id} - {cate.name}", help=str(d))
            st.json(d, expanded=False)
            st.session_state.cate = cate


viewer = Viewer()

# ------------------------------------------------------------
# col1
# c1 = col1.container(height=700)
c1 = col1

with c1.container(border=True):
    st.markdown("##### current:")
    viewer.select_cur_cate()

with c1.container(border=True):
    st.markdown("##### user")
    if st.button("all user (db)"):
        viewer.show_user_list()

    if st.button("add user (http)"):
        viewer.create_user()

with c1.container(border=True):
    st.markdown("##### category")
    if st.button("all category (db)"):
        viewer.show_category_list()

    if st.button("add category (http)"):
        viewer.create_category()

with c1.container(border=True):
    st.markdown("##### post")
    if st.button("all post (db)"):
        viewer.show_post_list()

    if st.button("add post (http)"):
        viewer.create_post()

# ------------------------------------------------------------
# col2
# c2 = col2.container(height=700)
c2 = col2

with c2.container(border=True):
    viewer.view_dataframe(st.session_state.users)

with c2.container(border=True):
    viewer.view_dataframe(st.session_state.cates)

with c2.container(border=True):
    viewer.view_dataframe(st.session_state.posts)
