from typing import List, Literal, TypedDict, Callable

Role = Literal["system", "user", "assistant"]


class Message(TypedDict):
    role: Role
    content: str


B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
DEFAULT_SYSTEM_PROMPT = """\
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""


def llama2_format_messages(messages: List[Message], tokenizer_encode: Callable) -> List[int]:
    if messages[0]["role"] != "system":
        messages = [
            {
                "role": "system",
                "content": DEFAULT_SYSTEM_PROMPT,
            }
        ] + messages
    messages = [
        {
            "role": messages[1]["role"],
            "content": B_SYS + messages[0]["content"] + E_SYS + messages[1]["content"],
        }
    ] + messages[2:]
    assert all([msg["role"] == "user" for msg in messages[::2]]) and all(
        [msg["role"] == "assistant" for msg in messages[1::2]]
    ), (
        "model only supports 'system', 'user' and 'assistant' roles, "
        "starting with 'system', then 'user' and alternating (u/a/u/a/u...)"
    )
    messages_tokens: List[int] = sum(
        [
            tokenizer_encode(
                f"{B_INST} {(prompt['content']).strip()} {E_INST} {(answer['content']).strip()} ",
                bos=True,
                eos=True,
            )
            for prompt, answer in zip(
                messages[::2],
                messages[1::2],
            )
        ],
        [],
    )
    assert messages[-1]["role"] == "user", f"Last message must be from user, got {messages[-1]['role']}"
    messages_tokens += tokenizer_encode(
        f"{B_INST} {(messages[-1]['content']).strip()} {E_INST}",
        bos=True,
        eos=False,
    )
    return messages_tokens
