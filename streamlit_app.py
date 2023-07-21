import os
from llama_cpp_chat_completion_wrapper import Llama2ChatCompletionWrapper, Message
import streamlit as st


def console_print(message: Message) -> None:
    reset = "\033[00m"
    color_map = {
        "system": ("\033[1;35m", "\033[35m"),
        "user": ("\033[1;33m", "\033[33m"),
        "assistant": ("\033[1;31m", "\033[31m"),
        "assistant-before-post-process": ("\033[1;31m", "\033[31m"),
    }
    role_color, content_color = color_map[message["role"]]
    formatted_message = f"{role_color}{message['role'].upper()}{reset}> {content_color}{message['content']}{reset}"
    print(formatted_message)


@st.cache_resource
def load_model():
    model_path = os.path.join(os.environ["MODELS_PATH"], "TheBloke", "llama-2-7b-chat.ggmlv3.q2_K.bin")
    return Llama2ChatCompletionWrapper(model_path=model_path, callback=console_print)


def main():
    if len(st.session_state) == 0:
        st.session_state["llm"] = load_model()
        st.session_state["params"] = {
            "temp": 0,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
        }
        st.session_state["llm"].new_session()
        st.session_state["messages"] = st.session_state["llm"].messages

    st.title("💬 Chatbot")

    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.chat_message("user").write(prompt)
        response = st.session_state["llm"](prompt, params=st.session_state["params"])
        st.chat_message("assistant").write(response)


if __name__ == "__main__":
    main()
