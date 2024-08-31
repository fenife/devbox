import streamlit as st
import pandas as pd
import numpy as np

import shell
from engine import ShellResult

st.set_page_config(layout="wide")

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

with st.sidebar:
    st.markdown("# Main page")
                
    clear = st.button("clear shell")
    if clear:
        st.session_state.messages = []


col1, col2 = st.columns([1, 1], gap="small")
 
with col1:
    st.dataframe(df, width=800, height=500)  

with col2:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    c1 = st.container(height=600)
    for msg in reversed(st.session_state.messages):
        # c1.chat_message(msg["role"]).code(msg["content"])
        c1.code(msg["content"])

    if cmd := st.chat_input("command"):
        r = shell.run_cmd(cmd)
        st.session_state.messages.append({"role": "ai", "content": r.output})
        # c1.chat_message("ai").code(r.output)
        c1.code(r.output)
