from src.store_index import VectorStore
from src.helper import load_pdf_file, text_split

index_path = "faiss_index"
vecters = VectorStore(index_path)


data = load_pdf_file("Data/")
chunks = text_split(data)
vector_db = vecters.store_index(chunks)
print("Done.....")