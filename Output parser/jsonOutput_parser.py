from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age and city of ficional person. /n {format_instruction}', 
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
# In that type of parser we have to send additional information like which type of output you want '{format_instruction}'. And this input was tell by parser when we call this function get_format_instructions().

# We call format instruction to parcel variable because of It feel before the runtime like user don't tell. 

prompt = template.format() # Formate = invoke
# Here we doesn't need to give input or any prompt because in prompt template to be already give it. it act like a static prompt

print(prompt)

# Output
# Give me the name, age and city of ficional person. /n Return a JSON object. (Basically this is the prompt that we send to out Llm)

result = model.invoke(prompt)

finel_result = parser.parse(result.content[0]['text'])

print(finel_result)
print(type(finel_result))

# Output 
# {'name': 'Elena Vance', 'age': 29, 'city': 'Silverpine'}
# <class 'dict'>

# Using chain
chain = template | model | parser
result =  chain.invoke({}) # Here we have to give parenthesis because of Jane.invokemethod always need one parameter like one input variable but here there is no input variable so we need empty parenthesis
print(result)