# we use this when we have to use API of HuggingFace
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint   
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    # Which model you have to use , give here in repo_id
    repo_id="zai-org/GLM-5.3",

    # here we have to pass , which task we have to perform for example text-generation, text2text-generation, text-classification etc.
    task="text-generation"
)

model = ChatHuggingFace(llm=llm) # here we have to pass llm which we have to configure with HuggingFaceEndpoint.

result = model.invoke("What is the capital of India?")

print(result.content)