def search_chunks(collection, question, n_results=3):
    """
    Find the most relevant document chunks
    for the user's question.
    """

    total_chunks = collection.count()

    if total_chunks == 0:
        return []

    # Do not request more results than available chunks.
    n_results = min(n_results, total_chunks)

    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )

    retrieved_chunks = results["documents"][0]

    return retrieved_chunks