# llama_cpp Chat completion wrapper

Handles chat completion message format to use with [llama-cpp-python](https://github.com/abetlen/llama-cpp-python).
Basically, the code was got from [here](https://github.com/facebookresearch/llama/blob/main/llama/generation.py#L212).

NOTE: It's still not identical to Meta's original [functionality](https://github.com/facebookresearch/llama/blob/main/llama/generation.py#L212). See Issues section!

## Installation

Developed using `python 3.10` on windows.

```bash
pip install -r requirements.txt
```

## Usage

TODO

## Resources

TODO

## Issues

There are several discussions around the chat format [[1](https://huggingface.co/TheBloke/Llama-2-13B-chat-GPTQ/discussions/5), [2](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/discussions/3), [3](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/discussions/4), [4](https://github.com/ggerganov/llama.cpp/issues/2262#issuecomment-1641323686), [5](https://huggingface.co/TheBloke/Llama-2-70B-chat-GPTQ/discussions/7), [6](https://gpus.llm-utils.org/llama-2-prompt-template/), [7](https://github.com/abetlen/llama-cpp-python/issues/507)].

Currently I'm working on that. The notebook `llama_cpp_vs_meta.ipynb` shows the comparison discrepancy I'm facing now. If you have any tip on that, it'll be very welcome!



