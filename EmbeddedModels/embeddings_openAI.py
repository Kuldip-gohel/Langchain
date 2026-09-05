from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimension=32)
# in vector output howmany dimession you want just tell that here.

result = embedding.embed_query("Delhi is the capital of india")
# In embed query, we just give query/prompt, it will go in embedding model -> process --> generate vector with 32 dimension and return the vector output. 

print(result)
print(str(result))


# if vector is small then it cover little contextual meaning ,but if vector is large then it cover more contextual meaning.