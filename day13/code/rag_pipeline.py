from embed_store import EmbedStore
from query_engine import QueryEngine


class RAGPipeline:
    """A simple Retrieval-Augmented Generation pipeline"""
    def __init__(self):
        self.store = EmbedStore()
        self.engine = QueryEngine(self.store)

    def ingest(self, doc_id, text):
        """Ingest a document into the vector store"""
        self.store.store_document(doc_id, text)

    def query(self, question, top_k=3):
        """Ask a question and get a RAG answer"""
        return self.engine.answer(question, top_k=top_k)
