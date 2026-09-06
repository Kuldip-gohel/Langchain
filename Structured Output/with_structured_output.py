from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

# Schema
class review(TypedDict):

    # Annoteded , give some more discription about prompt or schema so model easily undersatand it.

    summary: Annotated[str, "A brief summary of the riview."]
    sentiment: Annotated[str, "Return sentiment of review, Either Negative, positive, nutral"]


# Now this model have defination of this schema
structured_model = model.with_structured_output(review) 


result = structured_model.invoke("""
The hardware is greate but softmere feels bloated. There are too many pre-installed apps that I cant remove. Also, the UI looks outdeted compared to other brands. Hopping for a software update to fix this.
""")

print(result)
print(result['summary'])
print(result['sentiment'])

#  Output,
# {'summary': 'The user praises the hardware but expresses frustration with bloated software, unremovable pre-installed apps, and an outdated user interface, hoping for a future software update.', 'sentiment': 'Mixed'}