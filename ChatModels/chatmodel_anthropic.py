from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-v1', temperature= 0.7, max_completion_tokens=10) 

result = model.invoke('What is the capital of India?')

print(result.content)