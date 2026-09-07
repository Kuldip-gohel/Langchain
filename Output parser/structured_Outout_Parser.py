# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain.output_parsers import StructuredOutputParser, ResponseSchema
# # This library from Liangcheng.output pars it is not working in this model because it's a old Library that used in old version so currently we have to use identic and with structured output model like downward code.

# load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

# schema = [
#     ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
#     ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
#     ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
# ]

# parser  = StructuredOutputParser.from_response_schema(schema)

# template = PromptTemplate(
#     template='give 3 facts about the {topic} \n {format_instruction}',
#     input_variables=['topic'],
#     partial_variables={'format_instruction':parser.get_format_instruction()}
# )

# chain = template |model | parser
# result = chain.invoke({'topic':'black hole'})
# print(result)















from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

class Facts(BaseModel):
    fact_1: str = Field(description="Fact 1 about the topic")
    fact_2: str = Field(description="Fact 2 about the topic")
    fact_3: str = Field(description="Fact 3 about the topic")

structured_model = model.with_structured_output(Facts)

result = structured_model.invoke("Give me 3 facts about black holes.")
print(result)

# Output ,
# fact_1='Black holes are regions of spacetime where gravity is so strong that nothing, including light and other electromagnetic waves, has enough energy to escape it.' fact_2='The boundary surrounding a black hole beyond which no light or matter can escape is called the event horizon.' fact_3='Supermassive black holes containing millions or billions of times the mass of the Sun are believed to exist at the centers of most galaxies, including the Milky Way.'