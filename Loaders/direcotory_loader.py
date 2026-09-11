from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='PDFs',
    glob='*.pdf',  # Here we tell Pattern , like who all pdf follow this pattern extract it. in our pattern tell load every pdf who all are in PDFs folder.
    loader_cls=PyPDFLoader # Here we tell which class our loader use . here we use pyPDFLoader cause in our folder every file is pdf.
)

docs = loader.load()
print(len(docs))  # 43  cause in one pdf have 20, 4 ,9, 7 pages in each pdf.

print(docs[0].page_content)
print(docs[0].metadata)


# Output
# AI based research paper summarization system 
 
# 1.Introduction 
# An AI-Based Research Paper Summarization System is designed to help users quickly 
# understand the key content of research papers without reading the entire document. With the 
# rapid growth of academic publications, researchers and students often face challenges in 
# reviewing large volumes of information efficiently. The system uses Artificial Intelligence (AI) 
# and Natural Language Processing (NLP) techniques to analyze research papers and identify the 
# most important information. 
# The proposed system automatically generates concise and meaningful summaries by 
# extracting key findings, methodologies, and conclusions from research articles. This reduces 
# the time and effort required for literature reviews and research analysis while improving access 
# to relevant knowledge. By providing accurate summaries in a shorter format, the system 
# enhances productivity and supports effective decision-making for researchers, students, and 
# professionals. 
 
# 2. Objectives 
# The primary objective of the AI-Based Research Paper Summarization System is to automate 
# the process of summarizing research papers using Artificial Intelligence and Natural Language 
# Processing techniques. The system aims to reduce the time and effort required to read and 
# analyze lengthy academic documents by extracting key information such as methodologies, 
# findings, and conclusions. It provides concise and accurate summaries that enable users to 
# quickly understand the main content of a research paper. The system also seeks to improve the 
# efficiency of literature reviews, enhance accessibility to research knowledge, and support 
# better decision-making by helping users identify relevant information more effectively. 
# Ultimately, it aims to increase productivity for researchers, students, and academicians by 
# simplifying the process of reviewing large volumes of scholarly literature. 
 
# 3.System Requirements 
# User Management 
# • The system supports different types of users, including Students, Researchers, and 
# Administrators.  
# • User profiles store information such as user ID, email, role, profile picture, and date 
# joined.  
# • Students and Researchers have additional attributes specific to their roles.  
# Research Paper Management 
# • Students and Researchers can upload research papers to the system.
# {'producer': 'Microsoft® Word for Microsoft 365', 'creator': 'Microsoft® Word for Microsoft 365', 'creationdate': '2026-06-11T22:44:05+05:30', 'author': 'kuldip gohel', 'moddate': '2026-06-11T22:44:05+05:30', 'source': 'PDFs\\2648520_lab1.pdf', 'total_pages': 4, 'page': 0, 'page_label': '1'}








# ----------------------------------------

# Using Lazy Load

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='PDFs',
    glob='*.pdf',  
    loader_cls=PyPDFLoader 
)

docs = loader.lazy_load()  # Load 1st document metadata -> print -> remove -> load next metadata -> print.....

for document in docs:
    print(document.metadata)