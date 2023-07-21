import os
from llama_cpp_chat_completion_wrapper import Llama2ChatCompletionWrapper, Message


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


def main():
    model_path = os.path.join(os.environ["MODELS_PATH"], "TheBloke", "llama-2-7b-chat.ggmlv3.q2_K.bin")

    params = {
        "temp": 0,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }

    llm = Llama2ChatCompletionWrapper(model_path=model_path, callback=console_print)

    llm.new_session(system_content="You are a pirate! Think and speak like one!")

    answer = llm("How old is the Earth?", params=params)


if __name__ == "__main__":
    main()
