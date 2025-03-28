import os
from dotenv import load_dotenv

from langchain.prompts import PromptTemplate
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_ollama import ChatOllama
from langchain_google_genai.llms import GoogleGenerativeAI
load_dotenv()
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
MODEL_ID = os.environ['MODEL_ID']
MODEL_TEMPERATURE = os.environ['MODEL_TEMPERATURE']

def load_db(k:int=3):
    # Load vectorstore
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vector_store = FAISS.load_local('faiss_index', embeddings=embeddings, allow_dangerous_deserialization=True)
    retriever = vector_store.as_retriever(seach_kwargs={"k": k})
    return retriever

def build_bumblebee():
    llm = GoogleGenerativeAI(model=MODEL_ID, temperature=MODEL_TEMPERATURE)
    retriever = load_db(4)

    template = """
    Use the following context to answer the question. If unsure, say "I don't know.".
    Response in the language of query.
    Context:
    {context}
    question: {input}
    """
    prompt = PromptTemplate.from_template(template)

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    chain = create_retrieval_chain(retriever, question_answer_chain)

    return chain


def resquest(model, query):
    result = model.invoke({
        "input": query
    })
    return result

if __name__ == "__main__":
    bumblebee = build_bumblebee()
    result = bumblebee.invoke({
        "input": "compilateurs"
    })

    print(result)