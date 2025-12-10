import chromadb
from sentence_transformers import SentenceTransformer


class EmbedStore:
    """Handles chunking, embedding, and storing documents in ChromaDB"""

    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("rag_collection")
        self.embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def chunk_text(self, text, size=300):
        """Splits text into chunks of specified word size"""
        words = text.split()
        return [" ".join(words[i:i + size]) for i in range(0, len(words), size)]

    def store_document(self, doc_id, text):
        """Embeds and stores document chunks into ChromaDB"""
        chunks = self.chunk_text(text)
        embeddings = self.embedder.encode(chunks)
        ids = [f"{doc_id}_{i}" for i in range(len(chunks))]

        self.collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=ids
        )
