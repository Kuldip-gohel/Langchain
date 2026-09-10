from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence , RunnablePassthrough, RunnableParallel

load_dotenv()

# passthrough = RunnablePassthrough()
# print(passthrough.invoke(2)) # 2

prompt1 = PromptTemplate(
    template='generate a small joke about {topic} ' ,
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-3.7-flash')

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='generate a small Explanation of above {text} ' ,
    input_variables=['text']
)


joke_gen_chain = RunnableSequence(prompt1, model, parser)


parrallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'explanation': RunnableSequence(prompt2, model, parser)
    }
)

final_chain = RunnableSequence(joke_gen_chain, parrallel_chain)

result = final_chain.invoke({'topic':'vollyball'})

print(result)


# output
# {'joke': 'Why are volleyball players so good at working in restaurants?\n\nBecause they know how to deliver a great **serve**!', 'explanation': 'This joke is a pun based on the double meaning of the word **"serve"**:\n\n* **In volleyball:** A **serve** is the initial hit that starts the play by sending the ball over the net.\n* **In a restaurant:** To **serve** means to wait on tables and deliver food and drinks to customers.'}