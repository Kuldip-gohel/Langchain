from langchain_community.document_loaders import TextLoader 
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model="qwen3:8b")

prompt = PromptTemplate(
    template="Write 5 line summary of {topic}" , 
    input_variables=['topic']  
)

parser = StrOutputParser()

# Make Document Loader object
loader = TextLoader('cricket.txt', encoding='utf-8')
# Tell which encodeing formate it uses

doc = loader.load()
print(doc)
print(type(doc)) # List of document

print(len(doc))

print(doc[0])
print(type(doc[0]))  # Document

# Document conatins 2 things 
# print(doc[0].page_content)
# print(doc[0].metadata)

chain = prompt | model | parser

result = chain.invoke({'topic':doc[0].page_content})

print (result)


# output
# Beneath the sun or floodlight's gleam, cricket weaves a dream of unity, blending childhood joy with global passion. From dusty lanes to packed arenas, it binds nations through shared triumph and tension. The game’s rhythm—bat, ball, and bowler—echoes timeless tales of grit, glory, and heart. Legends and modern stars alike live by its code, etching memories into every run and catch. Cricket transcends sport, a universal thread connecting souls through the thrill of the chase.