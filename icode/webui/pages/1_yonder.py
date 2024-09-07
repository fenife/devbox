
from collections import namedtuple
import datetime
import json
import streamlit as st
from engine.db import DBClient, DBResult
from engine.http import HttpClient
from config import Config
from state.state import state
from view import viewer


st.set_page_config(layout="wide")


with st.sidebar:
    st.markdown("# Yonder page")
    if st.button("clear data"):
        state.clear_db_datas()

# ------------------------------------------------------------

spec = [1, 1, 1]
c_user, c_cate, c_post = st.columns(spec=spec, gap="small")


with c_user.container(border=True):
    st.markdown("##### user")
    if st.button("all user (db)"):
        viewer.get_users()

    if st.button("add user (http)"):
        viewer.create_user()

with c_cate.container(border=True):
    st.markdown("##### category")
    if st.button("all category (db)"):
        viewer.get_cates()

    if st.button("add category (http)"):
        viewer.create_category()

with c_post.container(border=True):
    st.markdown("##### post")
    if st.button("all post (db)"):
        viewer.get_posts()

    if st.button("add post (http)"):
        viewer.create_post()

# ------------------------------------------------------------

t_user, t_cate, t_page = st.tabs(["user", "category", "post"])


with t_user.container(border=True):
    viewer.show_users()

with t_cate.container(border=True):
    viewer.show_cates()

with t_page.container(border=True):
    viewer.show_posts()
