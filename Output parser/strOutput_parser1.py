# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

# Just made pipeline that 1st take template1 give it to model ., using parser it give only content , after give it it to trmplate 2 , then  provide prompt to model it will enerate summary.

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})
print(result)

# output
# 1. **Definition & Structure:** Black holes are regions of extreme gravity where nothing can escape past the event horizon, centered by a dense singularity and often encircled by superheated accretion disks.
# 2. **Types & Formation:** Ranging in scale from stellar-mass to supermassive, they primarily form through the gravitational collapse of dying massive stars, cosmic mergers, or early universe processes.
# 3. **Key Phenomena:** They induce extreme relativistic effects, such as gravitational time dilation and tidal spaghettification, while theoretically losing mass over time via Hawking radiation.
# 4. **Empirical Confirmation:** Once purely theoretical, black holes have been directly verified in recent years through gravitational wave detections by LIGO and direct shadow imaging by the Event Horizon Telescope.
# 5. **Frontiers in Physics:** Unresolved mysteries like the Information Paradox and the physical nature of singularities make black holes essential testing grounds for developing a theory of quantum gravity.


# Without parser we can make chain but in that we first get content from template 1 then give it to template2..