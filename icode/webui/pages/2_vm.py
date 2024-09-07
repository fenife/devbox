import streamlit as st
import pandas as pd
import numpy as np

from engine.shell import ShellResult
from view import vm_viewer
from vm import vm
from state.state import state


st.set_page_config(layout="wide")


with st.sidebar:
    st.markdown("# Shell page")

    clear = st.button("clear shell")
    if clear:
        state.clear_shells()


# ------------------------------------------------------------

t_local, t_vmc1, t_dev = st.tabs(["local", "vmc1", "dev"])


with t_local:
    vm_viewer.view_shells(label=vm.VM_LABEL_LOCAL)

with t_vmc1:
    vm_viewer.view_shells(label=vm.VM_LABEL_VMC1)
