import streamlit as st

from utils import read_data


def file_upload_form():
    load_options, datasets = {}, {}

    load_options["default_dataset"] = st.checkbox(
        "Load a default dataset", True, help="Load default dataset"
    )

    if load_options["default_dataset"]:
        df = read_data()
    else:
        existing_dataset = st.selectbox(
            "Choose from existing datasets",
            list(st.session_state["datasets"].keys()),
            index=None,
            placeholder="Select existing datasets...")

        if existing_dataset is not None:
            df = st.session_state["datasets"][existing_dataset]["data"]
            load_options = st.session_state["datasets"][existing_dataset]["load_options"]
        else:
            file = st.file_uploader("Choose a CSV file", type=["csv"], key="input_file_uploader")
            load_options["separator"] = st.selectbox(
                "What is the separator?", [",", ";", "|"], help="CSV Separator"
            )
            if file:
                df = read_data(file, load_options)
                st.session_state.datasets[file.name] = {"load_options": load_options, "data": df}
            else:
                df = read_data()
    return df, load_options
