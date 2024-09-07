from loguru import logger
from pandas.core.arrays.categorical import contains
import streamlit as st
from engine.db import DBClient, DBResult
from engine.http import HttpClient, HttpResult
from config import Config


class BaseViewer(object):

    def view_dataframe_query(self, data: DBResult):
        help_str = " f > 1 or f < 2 and f == 3 \n" \
                   " or f in (4, 5) and f.str.contains('a') "
        c = st.container()
        c_q, _ = c.columns(spec=[3, 1])
        query = c_q.text_input("query", key=f"df:input:query:{data.dt}",
                               help=help_str, placeholder=f"q: {help_str}")
        query_df = None
        if not query:
            return query_df
        try:
            logger.info("df query: %s" % query)
            st.text(f"df.query({query})")
            query_df = data.df.query(query)
        except Exception as e:
            c.warning(f"{str(e)}")
        return query_df

    def view_dataframe(self, data: DBResult):
        if not data:
            return

        df = data.df
        query_df = self.view_dataframe_query(data)
        st.write(data.dt, data.sql)
        if query_df is None:
            st.dataframe(df)
        else:
            st.dataframe(query_df)

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
