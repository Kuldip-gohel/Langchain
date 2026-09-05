# # from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# # from dotenv import load_dotenv
# from langchain_core.messages import SystemMessage, HumanMessage
# from langchain_core.prompts import ChatPromptTemplate

# chat_template = ChatPromptTemplate([
#     SystemMessage(content='You are a helpful {domain} expert'),
#     HumanMessage(content='Explain in simple term , what is {topic}')
# ])

# prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})
# print(prompt)
# # here it will print ,
# messages=[SystemMessage(content='You are a helpful {domain} expert', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple term , what is {topic}', additional_kwargs={}, response_metadata={})]

# # But problem is, it not fetch domain and topic so we use in differnt way that, 






# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
  ('system','You are a helpful {domain} expert'),
  ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})
print(prompt)

# # Now we can see
# messages=[SystemMessage(content='You are a helpful cricket expert', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms, what is Dusra', additional_kwargs={}, response_metadata={})]
