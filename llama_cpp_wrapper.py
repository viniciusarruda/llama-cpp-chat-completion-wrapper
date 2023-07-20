from llama_cpp import Llama
from typing import List


def llama_cpp_tokenizer_encode(s: str, bos: bool, eos: bool, llm: Llama) -> List[int]:
    assert type(s) is str
    t = llm.tokenize(text=bytes(s, encoding="utf-8"), add_bos=False)
    if bos:
        t = [llm.token_bos()] + t
    if eos:
        t = t + [llm.token_eos()]
    return t
