from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()
# print(docs)


# It will print page_content of 1st page 
print(docs[0].page_content)

# We use pypdf loader when we have mostly textual data , it not work well with images in pdf etc..