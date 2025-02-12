import streamlit as st
from io import StringIO
import requests

PORT = 8000
MICROSERVICE_HOST = "summarizer"
SERVICE_URL = f"http://{MICROSERVICE_HOST}:{PORT}/summarize"


@st.cache_data
def agent_process(string_data: str):
    # Send POST request
    try:
        payload = { "text": string_data }
        result = requests.post(SERVICE_URL, json=payload)
        if result.status_code == 200:
            return result.json()
        else:
            st.error(f"Error : {result.status_code}, {result.text}", icon="🚨")
    except Exception as exception:
        st.error(f"Error exception= {exception}", icon="🚨")
    return result


def load_text():
    return st.file_uploader("Choose a file")


def display_token_usage(dict_token):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("**Total tokens**")
        st.write(dict_token['total_tokens'])
    with col2:
        st.markdown("**Prompt tokens**")
        st.write(dict_token['prompt_tokens'])
    with col3:
        st.markdown("**Cached prompt tokens**")
        st.write(dict_token['cached_prompt_tokens'])
    with col4:
        st.markdown("**Completion tokens**")
        st.write(dict_token['completion_tokens'])
    with col5:
        st.markdown("**Successful requests**")
        st.write(dict_token['successful_requests'])


uploaded_file = load_text()
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    json_result = agent_process(string_data)
    if json_result is not None:
        col1, col2 = st.columns(2)
        with st.container():
            # st.markdown(f"**{json_result}**")
            with col1:
                st.markdown("**Original text**")
                with st.container():
                    st.write(string_data)

            with col2:
                st.markdown("**Result**")
                with st.container():
                    st.markdown(json_result["title"])
                    st.divider()
                    st.write(json_result["period"])
                    st.divider()
                    st.write(json_result["abstract"])

