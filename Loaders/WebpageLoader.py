from langchain_community.document_loaders import  WebBaseLoader
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model="qwen3:8b")

prompt = PromptTemplate(
    template="Write 5 line summary of {topic}" , 
    input_variables=['topic']  
)

parser = StrOutputParser()


url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
loader = WebBaseLoader(url)  # Using beautifulsup it will remove html tags and give only text content.

docs = loader.load()
# print(docs[0].page_content)

chain = prompt | model | parser

result = chain.invoke({'topic':docs[0].page_content})

print(result)


# Output
### **Core Concepts in AI**
# 1. **Key Areas**:
#    - **Language Models**: Large Language Models (LLMs) like **GPT**, **Claude**, **Gemini**, and **Llama**.
#    - **Techniques**: 
#      - **NLP/NLG** (Natural Language Processing/Generation)
#      - **Transformer** architecture, **Attention mechanisms**, **KV cache**, **Context window**
#      - **Training Methods**: Self-supervised learning, fine-tuning, RLHF (Reinforcement Learning from Human Feedback)
#    - **Applications**: 
#      - **Chatbots** (e.g., **ChatGPT**, **Claude**, **Kimi**)
#      - **AI Agents** (e.g., **AutoGPT**, **LangChain**)
#      - **Code Generation** (e.g., **OpenAI Codex**, **Vibe coding**)

# 2. **Model Types**:
#    - **Foundation Models** (e.g., **BLOOM**, **PaLM**, **Gemini**)
#    - **Small/Reasoning Models** (e.g., **Phi**, **Minerva**)
#    - **Multimodal Models** (e.g., **GPT-4**, **Gemini**)

# 3. **Hardware/Infrastructure**:
#    - **GPUs/TPUs** for training
#    - **High Bandwidth Memory (HBM)**, **Neural Processing Units (NPUs)**

# ---

# ### **Ethics, Regulation, and Risks**
# 1. **Regulation**:
#    - **Artificial Intelligence Act** (EU)
#    - **US Statement on AI Risk** (e.g., **Open letter on AI**, **Regulation of AI**)
#    - **Global Concerns**: Existential risk, AI safety, alignment with human values.

# 2. **Ethical Issues**:
#    - **Bias**, **Privacy**, **Environmental Impact**
#    - **Existential Risk** (e.g., **Superintelligence: Paths, Dangers, Strategies**, **The Precipice**)

# 3. **Societal Impacts**:
#    - **Job Displacement**, **AI Arms Race**, **AI Anthropomorphism**
#    - **Legal Challenges**: Copyright, liability for AI-generated content.

# ---

# ### **Key Organizations & People**
# - **Companies**: **OpenAI**, **Google DeepMind**, **Anthropic**, **Meta**, **Microsoft**, **Alibaba**, **NVIDIA**
# - **Research Institutions**: **MIT**, **Stanford**, **ETH Zurich**, **DeepMind**
# - **Notable Figures**:
#   - **Yoshua Bengio**, **Geoffrey Hinton**, **Yann LeCun** (Neural Networks)
#   - **Ilya Sutskever**, **Sam Altman**, **Demis Hassabis** (AI Leadership)
#   - **Niklas Luhmann**, **Heinz von Foerster** (Cybernetics)

# ---

# ### **Cybernetics & Related Fields**
# - **Cybernetics**: Subfields include **control theory**, **computational neuroscience**, **second-order cybernetics**, and **sociocybernetics**.
# - **Interdisciplinary Links**:
#   - **Biological Cybernetics** (e.g., **Gregory Bateson**, **Margaret Mead**)
#   - **Neurocybernetics**, **Biosemiotics**, **Cybersemiotics**

# ---

# ### **Tools & Frameworks**
# - **Software**: **PyTorch**, **TensorFlow**, **Hugging Face**, **llama.cpp**, **vLLM**
# - **Datasets**: **Common Crawl**, **The Pile**, **Web Scraping**, **Synthetic Data**
# - **Evaluation**: **MMLU**, **Humanity's Last Exam**, **GPTZero** (AI detection tools)

# ---

# ### **Challenges & Future Directions**
# - **Technical**: 
#   - **Model Compression** (e.g., **Knowledge Distillation**, **Speculative Decoding**)
#   - **Mechanistic Interpretability** (understanding model behavior)
# - **Societal**:
#   - **AI Governance**, **Global Collaboration**, **Mitigating Risks** (e.g., **AI Alignment**, **AI Safety**)

# ---

# This summary captures the breadth of AI, from foundational concepts to ethical and technical challenges, while linking to related fields like cybernetics and data science. Let me know if you'd like a deeper dive into a specific area!