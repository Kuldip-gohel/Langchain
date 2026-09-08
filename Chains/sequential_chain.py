from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a 5 pointer summary from following text \n {text}",
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'vollyball'})
print(result)

# output

# * **Origins and Global Reach:** Invented in 1895 by William G. Morgan as a non-contact YMCA recreation named "Mintonette," volleyball has evolved into a premier global Olympic sport governed by the FIVB, boasting over 900 million fans worldwide.
# * **Court Setup and Equipment:** Indoor matches are played on an $18\text{ m} \times 9\text{ m}$ court divided by a net ($2.43\text{ m}$ for men, $2.24\text{ m}$ for women) with a 3-meter attack line separating front-row and back-row zones.
# * **Core Rules and Scoring:** Two teams of six players rotate clockwise on side-outs and have up to three touches to return the ball over the net; matches follow a best-of-five rally-point format (sets 1–4 to 25 points, tiebreak to 15 points, winning by at least 2).
# * **Specialized Positions and Skills:** The game relies on sequential fundamentals (serving, passing, setting, spiking, blocking, digging) performed by specialized positions, including the playmaking Setter, offensive Hitters/Blockers, and the defensive Libero.
# * **Variations and Modern Play:** Alongside official adaptations like Beach and Sitting volleyball, modern competitive volleyball is characterized by extreme vertical athleticism, rapid offensive tempos, video review systems, and in-depth data analytics.