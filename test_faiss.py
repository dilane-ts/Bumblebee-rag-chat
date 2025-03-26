from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vector_store = FAISS.load_local('faiss_index', embeddings=embeddings, allow_dangerous_deserialization=True)

retriever = vector_store.as_retriever(search_kwargs={"k": 10})
docs = retriever.get_relevant_documents("Declarative programming")

for doc in docs:
    print("=============================================================")
    print(doc.page_content)
    print("=================================================\n")