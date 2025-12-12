from rag_pipeline import RAGPipeline

# Sample dummy text for ingestion
text = """
Transformers are deep learning architectures built on self-attention.
Large Language Models (LLMs) like GPT and LLaMA use transformers.
RAG enhances LLMs by providing external knowledge through retrieval.
It reduces hallucinations and improves factual accuracy.
"""

def main():
    rag = RAGPipeline()

    print("Ingesting document...")
    rag.ingest("doc1", text)

    print("\n--- RAG Query Result ---\n")
    response = rag.query("What is RAG?")
    print(response)


if __name__ == "__main__":
    main()
