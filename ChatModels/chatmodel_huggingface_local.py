from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# Normally it will download in C drive but if we want in another file then,
import os
os.environ['HF_HOME'] = 'D:/huggingface_cache'
# Also we run 2nd time it will not download again because it will check in the above path if it is already downloaded or not.


# when we run it , whatever model we use, it will download all things like configrization, tokenizer, model etc. and then it will Load in our RAM and run the model on local machine.
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"max_length": 100, "temperature": 0.7}
)

model = ChatHuggingFace(llm=llm) # Same first configure llm as above we do.

result = model.invoke("What is the capital of India?")
print(result.content)
