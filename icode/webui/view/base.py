import streamlit as st
from engine.db import DBClient, DBResult
from engine.http import HttpClient, HttpResult
from config import Config


class BaseViewer(object):
    def view_dataframe(self, data: DBResult):
        if data:
            st.write(data.dt, data.sql)
            st.dataframe(data.df)

    def view_http_result(self, r: HttpResult):
        if r is None:
            return 
        with st.container(border=True):
            st.write("request:")
            st.code(r.curl(), wrap_lines=True)
            st.write("response:")
            st.json(r.json())

    # def select_cur_cate(self):
    #     with st.container(border=True):
    #         cate = st.selectbox(label="category", index=None,
    #                             options=yonder.get_select_cates(),
    #                             format_func=_format_select_label)
    #         if not cate:
    #             return
    #         d = dict(zip(cate._fields, map(str, list(cate))))
    #         # st.text(f"cate: {cate.id} - {cate.name}", help=str(d))
    #         st.json(d, expanded=False)
    #         st.session_state.cate = cate
