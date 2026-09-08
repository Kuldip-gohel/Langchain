from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

llm = HuggingFaceEndpoint(
    repo_id='zai-org/GLM-5.3',
    task='text-generation'
)
model2 = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template='generate short and simple notes from the following \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="generate 5 short questions answer from the following text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="merge the provided notes and quiz into a single document \n {notes} and {quiz}",
    input_variables=['notes','quiz']
)

parser = StrOutputParser()


# Using parallel chain we can run multiple chain inside it.
parralel_chain = RunnableParallel(
    {
        'notes': prompt1 | model1 | parser ,
        'quiz': prompt2 | model2 | parser
    }
)

merge_chain = prompt3 | model1 | parser

chain = parralel_chain | merge_chain

text = """Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64."""

result = chain.invoke({'text':text})
print(result)

# output
## 📖 Part 1: Summary Notes

# ### **Overview**
# * **Type:** Supervised Learning algorithm.
# * **Primary Uses:** Classification, Regression, and Outlier detection.

# ---

# ### **Advantages (Pros)**
# * **High-Dimensional Performance:** Effective in high-dimensional spaces, even when the number of features ($p$) is greater than the number of samples ($n$).
# * **Memory Efficient:** Uses only a subset of key training points in the decision function (known as **support vectors**).
# * **Versatile:** Supports various standard (linear, polynomial, RBF) and custom **Kernel functions**.

# ---

# ### **Disadvantages (Cons)**
# * **Overfitting Risk:** Prone to overfitting if the number of features is significantly greater than the number of samples (requires careful tuning of kernels and regularization parameters).
# * **No Direct Probabilities:** Does not calculate probability estimates directly; obtaining them requires expensive 5-fold cross-validation.

# ---

# ### **Technical / Scikit-Learn Notes**
# * **Data Support:** Compatible with both **dense** (`numpy`) and **sparse** (`scipy`) matrices.
# * **Optimal Setup:** 
#   * **Data type:** `dtype=float64`
#   * **Dense matrices:** C-ordered `numpy.ndarray`
#   * **Sparse matrices:** `scipy.sparse.csr_matrix`

# ---

# ## ❓ Part 2: Review Quiz

# **Q1: What are Support Vector Machines (SVMs) used for?**  
# **A1:** SVMs are supervised learning methods used for classification, regression, and outlier detection.

# **Q2: Why are SVMs considered memory efficient?**  
# **A2:** Because they use only a subset of training points (called *support vectors*) in the decision function.

# **Q3: What is a key advantage of SVMs regarding Kernel functions?**  
# **A3:** They are versatile—standard common kernels are provided out-of-the-box, and custom kernels can also be specified.

# **Q4: What must be avoided when the number of features is much greater than the number of samples?**  
# **A4:** Overfitting, which is managed by carefully choosing appropriate Kernel functions and tuning the regularization term.

# **Q5: How do SVMs provide probability estimates, and what is the drawback?**  
# **A5:** They do not directly provide probability estimates; these must be calculated using an expensive 5-fold cross-validation process.
# (venv) PS D:\Langchain\Chains> 
