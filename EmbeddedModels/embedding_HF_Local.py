from langchain_huggingface import HuggingFaceEmbeddings

# here it downloads model and use it.
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# text = "Delhi is the capital of India."

# Now, let use multiple query/Documents.
documents = [
    "Delhi is the capital of India.",
    "Mumbai is the financial capital of India.",
    "Paris is the capital of France."
]

# vector = embedding.embed_query(text)
vector = embedding.embed_documents(documents)

print(vector)
print(str(vector))





# We can use OpenAI mbedding also cause it no more costly like 1M Embeddings in only 1 rupees.