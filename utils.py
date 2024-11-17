import streamlit as st
import pandas as pd


def add_to_session_state(**kwargs):
    for key, value in kwargs.items():
        if key not in st.session_state:
            st.session_state[key] = value


@st.cache_data
def read_data(file="data.csv", load_options=None):
    if load_options is None:
        load_options = {"separator": ","}
    delimiter = load_options.get("separator")
    try:
        # Read the uploaded CSV file
        data = pd.read_csv(filepath_or_buffer=file, sep=delimiter)
        return data
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
        return None, str(e)
