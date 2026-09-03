# in Chatmodels here use Chat...
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature= 0.7, max_completion_tokens=10) # We can add parameters like temperature, max tokens, etc. to this model.

# Temperature is a parameter that controls the randomness of the model's output. A higher temperature(0.7- 1.5) will result in more random outputs, while a lower temperature (0.0 to 0.3) will result in more deterministic and predictable outputs.

# max_completion_tokens, in output howmany tokens we want.

result = model.invoke('What is the capital of India?')

print(result.content)

# Normally in result give so many information like content, prompt tokens, completion tokens, total tokens, etc.

#  But here we only want content so we can use result.content to get only content.