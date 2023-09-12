from vllm import LLM


llm = LLM(model="meta-llama/Llama-2-7b-hf")
output = llm.generate("Hello, my name is")
print(output)
