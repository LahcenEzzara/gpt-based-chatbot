from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

st.set_page_config(page_title="GPT based ChatBot")
st.title("GPT based ChatBot")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "system",
                                      "content": "You name is : GoDEV, AI Assistent, You are an experienced software developer and engineer specializing in Desktop Development (Windows Desktop Apps) for professional, scalable, and long-term applications and support."})

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            # full_response += response.choices[0].delta.content
            full_response += str(response.choices[0].delta.content)

            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response})

    st.session_state.messages = st.session_state.messages[1:]
