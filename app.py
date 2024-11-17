import streamlit as st
import pandas as pd

from components.inputs import file_upload_form
from utils import read_data, add_to_session_state
from PIL import Image

st.set_page_config(page_title="Page Pilot", layout="wide")

add_to_session_state(df=read_data(), datasets={})

st.sidebar.title("Dataset")
with st.sidebar.expander("Dataset Upload", expanded=True):
    df, load_options = file_upload_form()

st.title("Part Pilot")
st.write("")

dataframe_event = st.dataframe(df,
                               use_container_width=True,
                               hide_index=True,
                               on_select="rerun",
                               selection_mode="multi-row", )

selected_ros = dataframe_event.selection.rows
filtered_df = df.iloc[selected_ros]

if len(selected_ros) > 0:
    st.write(f"Selected Rows : {len(selected_ros)}")

    st.subheader("Filtered Rows")

    st.dataframe(filtered_df,
                 use_container_width=True,
                 hide_index=True)
