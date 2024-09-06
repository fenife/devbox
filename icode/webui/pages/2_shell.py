import streamlit as st
import pandas as pd
import numpy as np

import shell
from engine.shell import ShellResult

st.set_page_config(layout="wide")

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

with st.sidebar:
    st.markdown("# Shell page")
                
    clear = st.button("clear shell")
    if clear:
        st.session_state.messages = []


col1, col2 = st.columns([1, 1], gap="small")


@st.dialog("Cast your form")
def vote(item):
    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)
 
with col1:
    # st.dataframe(df, width=800, height=500)  
    if st.button("form"):
        vote("form")

    with st.form("ls grep"):
        cmd = st.text_input("command")
        grep = st.text_input("grep")
        if grep:
            cmd = f"{cmd} | grep {grep}"
        submit = st.form_submit_button()
        if cmd and submit:
            r = shell.run_cmd(cmd)
            st.session_state.messages.append({"role": "ai", "content": r.output})
            # c1.chat_message("ai").code(r.output)
            st.code(r.output)
        else:
            st.warning("empty input")


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
