import chromadb

from create_embeddings import create_embedding_function


# Create the persistent database.
chroma_client = chromadb.PersistentClient(
    path="chroma_db"
)

# Create the embedding function.
embedding_function = create_embedding_function()


def get_collection(file_hash):
    """
    Get or create a ChromaDB collection
    for a particular PDF.
    """

    collection_name = "pdf_" + file_hash[:32]

    collection = chroma_client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function
    )

    return collection


def store_chunks(collection, chunks):
    """
    Store document chunks in ChromaDB.
    """

    if not chunks:
        raise ValueError(
            "No chunks available to store."
        )

    # Avoid inserting the same chunks repeatedly.
    if collection.count() > 0:
        return

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks
    )