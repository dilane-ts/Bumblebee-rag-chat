import os
from dotenv import load_dotenv

from langchain.prompts import PromptTemplate
from huggingface_hub import InferenceClient
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.language_models import LLM
from pydantic import Field, PrivateAttr
from langchain.chains import RetrievalQA

load_dotenv()
MODEL_ID = os.environ['MODEL_ID']
HF_TOKEN = os.environ['HF_TOKEN']

def load_db(k:int=3):
    # Load vectorstore
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vector_store = FAISS.load_local('faiss_index', embeddings=embeddings, allow_dangerous_deserialization=True)
    retriever = vector_store.as_retriever(seach_kwargs={"k": k})
    return retriever

class HuggingFaceInferrenceLLM(LLM):
    model: str
    api_key: str
    provider: str = Field(default='fireworks-ai')
    kwargs: dict = Field(default_factory=dict)
    _client: InferenceClient = PrivateAttr()

    def __init__(self, **data):
        super().__init__(**data)
        self._client = InferenceClient(provider=self.provider, api_key=self.api_key)

    @property
    def _llm_type(self) -> str:
        return "huggingface_inference"
    
    def _call(self, prompt, stop = None, callbacks = None, *, tags = None, metadata = None, **kwargs):
        response = self._client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            **self.kwargs
        )

        return response.choices[0].message.content
    



def build_bumblebee():
    llm = HuggingFaceInferrenceLLM(model=MODEL_ID, api_key=HF_TOKEN)

    retriever = load_db(4)

    prompt = PromptTemplate.from_template("""
    Use the following context to answer the question. If unsure, say "I don't know."
    Context:
    {context}
    Question: {question}
    Answer:
    """)

    bumblebee = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )

    return bumblebee


def resquest(model, query):
    result = model({
        "query": query
    })

    return result
