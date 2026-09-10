from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence , RunnablePassthrough, RunnableParallel, RunnableLambda, RunnableBranch
from langchain_ollama import ChatOllama

load_dotenv() 

prompt1 = PromptTemplate(
    template="Write detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}",
input_variables=['text']
)

model = ChatOllama(model="qwen3:8b")

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

barnch_chain = RunnableBranch(
    (lambda x:len(x.split())>100, RunnableSequence(prompt2, model, parser) ),
    RunnablePassthrough()
)

finel_chain = RunnableSequence(report_gen_chain, barnch_chain)

result = finel_chain.invoke({'topic':'Russia vs Ukrain'})

print(result)



# Output
# **Summary of "Russia vs. Ukraine: A Comprehensive Analysis" (October 2023)**  

# The Russia-Ukraine conflict, escalating into a full-scale war in February 2022, is a pivotal geopolitical crisis with profound global implications. Rooted in historical tensions, territorial disputes, and ideological divides, the war has drawn international attention, affecting security, humanitarian crises, and global alliances.  

# **Key Points:**  
# 1. **Historical Context**:  
#    - The conflict began in 2014 with Russia’s annexation of Crimea and the Donbas War, where pro-Russian separatists clashed with Ukrainian forces. The Minsk agreements (2014–2015) failed to resolve the crisis.  
#    - Russia’s 2022 full-scale invasion, justified as "denazification" and "demilitarization," aimed to occupy eastern Ukraine and Crimea.  

# 2. **Causes**:  
#    - **Geopolitical rivalry**: Russia views NATO expansion and Ukraine’s Western alignment as existential threats.  
#    - **Historical tensions**: Ukraine’s post-Soviet identity clashes with Russia’s imperial ambitions.  
#    - **Economic interests**: Ukraine’s strategic role in Europe’s energy infrastructure (e.g., Nord Stream pipelines) and Russia’s reliance on Ukrainian transit routes.  
#    - **Domestic politics**: Putin’s regime uses the war to consolidate power, while Ukraine’s public supports the defense of sovereignty.  

# 3. **Military Dynamics**:  
#    - **Three phases**:  
#      - **Phase 1 (2022)**: Russia’s initial advances stalled due to Ukrainian resistance and Western aid.  
#      - **Phase 2 (2022–2023)**: Stalemate with Ukrainian counteroffensives reclaiming territory in Kharkiv and Kherson.  
#      - **Phase 3 (2023)**: Escalation of attacks on cities, cyber warfare, and increased Western military support.  

# 4. **Humanitarian Impact**:  
#    - Over **10,000 civilian deaths**, **14,000+ Ukrainian soldiers killed**, and **10.7 million displaced** (5.5 million refugees).  
#    - Destruction of infrastructure, war crimes (e.g., Mariupol’s siege), and reports of starvation and forced deportations.  

# 5. **International Reactions**:  
#    - **Western sanctions**: Targeting Russia’s economy, energy sector, and oligarchs, leading to hyperinflation and isolation.  
#    - **Support for Ukraine**: $110 billion in aid (military, financial, and humanitarian) from the U.S., EU, and NATO.  
#    - **Neutral stances**: China avoids direct involvement, while countries like India and South Africa advocate for diplomacy.  

# 6. **Future Outlook**:  
#    - **Prolonged conflict**: Likely to continue with tactical stalemates and limited territorial gains.  
#    - **Peace talks**: Slow progress in negotiations (e.g., Moscow Format), with unresolved issues over sovereignty and territorial control.  
#    - **Global shifts**: Accelerated NATO expansion, energy diversification in Europe, and realignment of global power dynamics.  

# **Conclusion**: The war has reshaped international alliances, economies, and ethical debates about conflict. While Ukraine seeks sovereignty, the path to peace remains uncertain, underscoring the fragility of global order amid rising nationalism and technological warfare.  

# **Sources**: UN reports, NATO, Ukrainian Ministry of Defense, and international media.