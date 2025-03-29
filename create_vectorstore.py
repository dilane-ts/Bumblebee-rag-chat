from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.embeddings import SentenceTransformerEmbeddings



def load_documents(folder_path: str):

    loader = PyPDFDirectoryLoader(
        path=folder_path,
        glob='**/[!.]*.pdf',
        extract_images=False,
    )

    documents = loader.load()
    return documents

def create_vectorstore(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=64)
    split_docs = text_splitter.split_documents(documents)
    embeddings = SentenceTransformerEmbeddings()
    print(embeddings.model_name)
    vector_store = FAISS.from_documents(split_docs, embeddings)
    vector_store.save_local('faiss_index')

if __name__ == "__main__":
    folder_path = "./documents"
    documents = load_documents(folder_path)
    create_vectorstore(documents)