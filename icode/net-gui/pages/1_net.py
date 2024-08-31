import streamlit as st
import shell
from engine import ShellResult

st.sidebar.markdown("# Net page")

# with st.container(height=1000, border=True):
col1, col2 = st.columns(2, gap="small")
c1 = col1.container(height=500, border=True)
c2 = col2.container(height=500, border=True)

def ls_current_dir():
    r = shell.ls_current()
    c2.code(r.output)


c1.button("ls", on_click=ls_current_dir)

