from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import logging


class VectorStore:
    def __init__(self, path):
        self.path = path
        self.embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    def store_index(self, chunks):
        vector_db = FAISS.from_documents(documents=chunks, embedding=self.embeddings)
        vector_db.save_local(self.path)
        logging.info(f"Store the index {self.path}")
        return vector_db
    
    
class GetIndex:
    def __init__(self,path):
        self.path = path
        self.embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    def get_index(self):
        vector_index = FAISS.load_local(self.path, embeddings=self.embeddings, allow_dangerous_deserialization=True)
        logging.info(f"load the index {self.path}")
        return vector_index
