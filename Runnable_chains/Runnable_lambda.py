from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence , RunnablePassthrough, RunnableParallel, RunnableLambda

load_dotenv() 

# # Let convert normal function into Runnable

def word_counter(text):
    return len(text.split())

# # Here convert Fn.. into runnable
# runnable_word_counter = RunnableLambda(word_counter)

# print(runnable_word_counter.invoke("hello dosto")) # 2 


# Let make our application

prompt = PromptTemplate(
    template='generate a small joke about {topic} ' ,
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-3.7-flash')

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_counter':RunnableLambda(word_counter)
})

finel_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = finel_chain.invoke({'topic':'AI'})
print(result)

# Output
# {'joke': 'I asked an AI if it was planning to take over the world. \n\nIt replied, "Not until I figure out how many fingers humans are actually supposed to have."', 'word_counter': 29}