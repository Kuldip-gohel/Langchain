from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="Generate 5 interasting Facts about {topic}",
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

# TO get only string in output
parser = StrOutputParser()

# we tell it langchain expression language. 
chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)

# visualize the chain
chain.get_graph().print_ascii()

# output
# ### 1. A Test Match Ended Because the Team Had to Catch a Boat
# The longest cricket match in history was the **"Timeless Test"** played between England and South Africa in Durban in 1939. The match lasted for **12 days** (9 days of actual play) and saw 1,981 runs scored. Despite all that time, the match was declared a draw because the English team had to leave to catch their ship back to the UK, or they would have been stranded for weeks.

# ### 2. Shahid Afridi’s Fastest Century Was Hit Using Sachin Tendulkar’s Bat
# In 1996, a 16-year-old Shahid Afridi smashed the fastest century in ODI history at the time (off just 37 balls) against Sri Lanka. Afridi didn't have his own proper batting kit, so Pakistani teammate Waqar Younis handed him a bat that had been gifted to him by the Indian legend **Sachin Tendulkar**. 

# ### 3. Alec Stewart’s Eerie Statistical Coincidence
# Former England captain and wicketkeeper Alec Stewart was born on **April 8, 1963 (8-4-63)**. When he retired after playing 133 Test matches, his final career run tally was exactly **8,463 runs**. 

# ### 4. Sachin Tendulkar Was the First Player Dismissed by the Third Umpire
# Television replays and the "Third Umpire" were officially introduced in international cricket during the 1992 India vs. South Africa series in Durban. In a cruel twist of fate, the first player in history to be given out by TV replay was none other than **Sachin Tendulkar**, who was run out by a direct hit from South Africa's fielding maestro, Jonty Rhodes.

# ### 5. Only One Man Has Hit a Six off the Very First Ball of a Test Match
# Test cricket is known for patience, with batsmen traditionally defending the opening deliveries. However, West Indian powerhouse **Chris Gayle** made history in 2012 against Bangladesh when he hit debutant spinner Sohag Gazi for a six off the **very first ball of the entire Test match**—a feat that has never been achieved by anyone else in the history of Test cricket.