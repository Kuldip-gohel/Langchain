from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

# Pydentic object
class person(BaseModel):

    name: str = Field(description="name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city:str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person \n {format_instructions}",
    input_variables=['place'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

# prompt = template.invoke({'place':'indian'})
# result = model.invoke(prompt)
# finel_result = parser.parse(result.content)

chain  = template | model | parser
finel_result = chain.invoke({'place':'indian'})
print(finel_result)

# Output
# name='Aarav Patel' age=28 city='Bengaluru'


# Whatever prompt we give to the model using template prompt template in that it will first used text like generate the name and city of the fictional Indian person and tell the Jason to give format output like explain some technical things and name and description and a city what are the required things this all prompts are provided to model