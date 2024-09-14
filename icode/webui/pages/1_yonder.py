
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

t_user, t_cate, t_page = st.tabs(["user", "category", "post"])


with t_user.container(border=True):
    viewer.view_user_buttons()
    viewer.show_users()

with t_cate.container(border=True):
    viewer.view_cate_buttons()
    viewer.show_cates()

with t_page.container(border=True):
    viewer.view_post_buttons()
    viewer.show_posts()
