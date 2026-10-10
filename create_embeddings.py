from chromadb.utils import embedding_functions


def create_embedding_function():
    """
    Create the Sentence Transformer embedding function.
    """

    embedding_function = (
        embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
    )

    return embedding_function