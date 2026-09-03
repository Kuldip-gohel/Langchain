# Langchain understand how to communicate with openAi's API key
from langchain_openai import OpenAI

# Load secrete files from .env file
from dotenv import Load_dotenv

Load_dotenv() # Load OpenAI API key

# Make object
llm = OpenAI(model='gpt-3.5-turbo-instuct') # Work with this model

result =llm.invoke("What is the capital of India?") # Write any question/ prompt to the model and it will return the answer.
# Behind the scenes, invoke method will call model and give this prompt -> Model will process it and generate reply -> Give reply

print(result) 