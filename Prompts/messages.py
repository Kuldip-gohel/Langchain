from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

model = HuggingFaceEndpoint(repo_id='zai-org/GLM-5.3', task='text-generation')
model = ChatHuggingFace(llm=model)

messages = [
    SystemMessage(content="You are helpful assistant"),
    HumanMessage(content='Tell me about Langchain')
]

result = model.invoke(messages)
print(result.content)

# result convert in AIMessage nd append in messages.
messages.append(AIMessage(content=result.content))

# Print chat History
print(messages)

# It will print history in formate like, 
[SystemMessage(content='You are helpful assistant', additional_kwargs={}, response_metadata={}), HumanMessage(content='Tell me about Langchain', additional_kwargs={}, response_metadata={}), AIMessage(content='', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]