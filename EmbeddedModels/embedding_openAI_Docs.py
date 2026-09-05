from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimension=32)

# Now we see how we can generate embedding for multiple documents at once.
documents = [
    "Delhi is the capital of India.",
    "Mumbai is the financial capital of India.",
    "Paris is the capital of France."
]


# Here we call embed_documents method.
result = embedding.embed_documents(documents)

print(result)
print(str(result))


