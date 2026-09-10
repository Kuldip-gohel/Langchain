from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence , RunnableParallel
from langchain_ollama import ChatOllama


load_dotenv()

prompt1 = PromptTemplate(
    template='generate a small tweet about {topic} ' ,
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='generate a small linkdin post about {topic} ' ,
    input_variables=['topic']
)

model = ChatOllama(model="qwen3:8b")

parser = StrOutputParser()

parrallel_chain = RunnableParallel(
    {
        'tweet': RunnableSequence(prompt1, model, parser),
        'linkdin': RunnableSequence(prompt2, model, parser)
    }
)

result = parrallel_chain.invoke({'topic':'AI'})

print(result)
print(result['tweet'])
print(result['linkdin'])


# Output

# {'tweet': 'AI won’t replace human creativity—it will amplify it. The future belongs to those who learn to build *with* it, not fear it. 🤖✨ \n\n#AI #TechTrends', 'linkdin': 'Here are a few options depending on the vibe you want:\n\n### Option 1: Focus on Productivity & Mindset (Best overall)\nAI isn’t here to replace human creativity—it’s here to amplify it. 🚀\n\nThe real power of AI isn\'t just automation; it’s *augmentation*. \n\nBy letting smart tools handle repetitive tasks, we unlock more time for what truly matters:\n💡 Strategic thinking\n🎨 Creative problem-solving\n🤝 Building real human connections\n\nThe future doesn’t belong to AI alone. It belongs to the people who learn to collaborate with it.\n\nHow are you leveraging AI in your daily workflow? 👇\n\n#ArtificialIntelligence #FutureOfWork #Productivity #Innovation #TechTrends\n\n---\n\n### Option 2: Short & Punchy\nThe biggest misconception about AI right now:  \n*"It\'s going to replace professionals."*\n\nThe reality:  \nAI won\'t replace you. But a professional using AI just might. \n\nThink of it as the ultimate co-pilot, not the pilot. \n\nAre you using AI to speed up your work, or are you still sitting on the sidelines?\n\n#AI #CareerGrowth #Technology #Leadership'}
# AI won’t replace human creativity—it will amplify it. The future belongs to those who learn to build *with* it, not fear it. 🤖✨ 

# #AI #TechTrends
# Here are a few options depending on the vibe you want:

# ### Option 1: Focus on Productivity & Mindset (Best overall)
# AI isn’t here to replace human creativity—it’s here to amplify it. 🚀

# The real power of AI isn't just automation; it’s *augmentation*. 

# By letting smart tools handle repetitive tasks, we unlock more time for what truly matters:
# 💡 Strategic thinking
# 🎨 Creative problem-solving
# 🤝 Building real human connections

# The future doesn’t belong to AI alone. It belongs to the people who learn to collaborate with it.

# How are you leveraging AI in your daily workflow? 👇

# #ArtificialIntelligence #FutureOfWork #Productivity #Innovation #TechTrends

# ---

# ### Option 2: Short & Punchy
# The biggest misconception about AI right now:  
# *"It's going to replace professionals."*

# The reality:  
# AI won't replace you. But a professional using AI just might. 

# Think of it as the ultimate co-pilot, not the pilot. 

# Are you using AI to speed up your work, or are you still sitting on the sidelines?

# #AI #CareerGrowth #Technology #Leadership
