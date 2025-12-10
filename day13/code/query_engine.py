from transformers import pipeline


class QueryEngine:
    """Handles query embedding, retrieval and LLM-based answer generation"""

    def __init__(self, store):
        self.store = store
        self.llm = pipeline("text-generation", model="gpt2")

    def answer(self, query, top_k=3):
        """Generates an answer based on retrieved context"""
        query_embedding = self.store.embedder.encode([query])[0]

        results = self.store.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        context = "\n\n".join(results["documents"][0])

        prompt = f"Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"

        output = self.llm(prompt, max_length=200, do_sample=False)
        return output[0]["generated_text"]
