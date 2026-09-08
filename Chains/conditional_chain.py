from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import  RunnableBranch, RunnableLambda # Use in conditions based chains, RunnableLambda convert lambda function into runnable and we use it like chain
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

parser = StrOutputParser()

# We have to create class because of sometimes output may be this is a negative or this is a positive or also some time away it is case sensitive so using this way get structure output like only positive or negetive
class Feedback(BaseModel):

    sentiment: Literal['positive','negative'] =Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='classify the sentimant of the following feedback text into positive or negative \n {feedback} \n {formate_instruction}',
    input_variables=['feedback'],
    partial_variables={'formate_instruction':parser2.get_format_instructions()}
)

classifie_chain = prompt1 | model | parser2

# Just make 2 prompts for Each Branch
prompt2 = PromptTemplate(
    template="write an appropriate response to this positive feedback in 2 lines \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="write an appropriate response to this negetive feedback in 2 lines \n {feedback}",
    input_variables=['feedback']
)


# in Runablle branch we have to provide multiple Tupple, in that we have to pass condition and 2nd if condition was true then which chain you want to execute. 
branch_chain = RunnableBranch(
    # If value positive then trigger this chain
    (lambda x:x.sentiment=='positive', prompt2 | model | parser),
    (lambda x:x.sentiment=='negetive', prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment")
)
# At last we have to rovide default chain, here lambda function is not chain so we have to convert it into chain using Runnablelambda.

chain = classifie_chain | branch_chain

result = chain.invoke({'feedback':'This is Good phone'})

print(result)


# Output
# Thank you so much for your kind words and support! 
# We're thrilled to hear you had a great experience and look forward to serving you again soon.