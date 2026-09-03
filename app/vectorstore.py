# turning chunks into vectors and storing them in database(chromadb)
import chromadb
from chromadb.utils import embedding_functions

# client is an object that represents your connectionm to the service (CHROMADB)
client = chromadb.PersistentClient(path="./data/chroma_db")

# builds an embedding function powered by (all-MiniLM-L6-v2) model - turns text into numeric vectors
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

collection = client.get_or_create_collection(name="documents", embedding_function=embedding_fn,)


# insert a batch of text chunks into the collection
def add_chunks(doc_id: str, chunks: list[str]):
    # build a unique ID per chunk handbook.txt_0 , handbook.txt_1
    ids = [f"{doc_id} {i}" for i in range(len(chunks))]
    # [handbook.txt chunk 2]
    metadatas = [{"source": doc_id, "chunk_index": i} for i in range(len(chunks))]
    # insert everything into ChromaDB 
    collection.add(documents=chunks, metadatas=metadatas, ids=ids)
    return len(chunks)

def search_chunks(query: str, top_k: int = 4):
    return collection.query(query_texts=[query], n_results=top_k)