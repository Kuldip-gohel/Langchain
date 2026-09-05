# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="zai-org/GLM-5.3", task="text-generation")
model = ChatHuggingFace(llm=llm)

chat_History = [
    SystemMessage(content="You are a heplful AI assistant")
]


while True:
    user_input = input('You: ') 
    chat_History.append(HumanMessage(content=user_input)) # Convert user input into HUmmanmessage
    if user_input == 'exit':
        break
    result = model.invoke(chat_History)
    chat_History.append(AIMessage(content=result.content)) # Convert result into AI message
    print("AI: ",result.content)

print(chat_History)

# here problem was in our chathistory all things input and output store in one list
# how can we find which is input and output ?

# Using 3 types of messages we solve the problem.