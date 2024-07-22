import streamlit as st
import openai

# Streamlit application
st.set_page_config(page_title="Indoor Tennis Courts Finder", 
page_icon=":tennis:", 
layout='centered')

st.title('Indoor Tennis Court Finder')

# Input for OpenAI API Key
st.sidebar.title("Settings")
api_key = st.sidebar.text_input('Enter your OpenAI API Key', value='', type='password')

if api_key:
    openai.api_key = api_key

    # Placeholder for OpenAI generated responses
    response_area = st.empty()

    # User query
    user_query = st.text_input('Find an indoor tennis court:')
    if user_query:
        st.warning('Please wait...Analyzing...')
        # Create conversation with OpenAI's GPT model
        response = openai.ChatCompletion.create(
            model="gpt-3", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"find {user_query}"},
            ],
        )
        message_content = response.choices[0].message.content.strip()
        response_area.markdown(message_content)

    # Add some CSS styles
    st.markdown("""
                <style>
                body {
                    color: #fff;
                    background-color: #4f8bf9;
                }
                </style>
                """, unsafe_allow_html=True)