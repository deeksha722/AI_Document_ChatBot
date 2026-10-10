def chunk_text(text, chunk_size=100):
    """
    Split text into chunks of words.

    chunk_size: Maximum number of words per chunk.
    """

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(
            words[i:i + chunk_size]
        )

        chunks.append(chunk)

    return chunks