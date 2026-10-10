import hashlib
import streamlit as st

from ui import (
    apply_design,
    render_header,
    render_sidebar,
    render_empty_state,
    render_chat_history,
    render_footer
)

from read_pdf import read_pdf
from chunk_text import chunk_text
from store_chunks import get_collection, store_chunks
from search_chunks import search_chunks
from generate_answer import generate_answer


# ---------------- PAGE DESIGN ----------------

apply_design()


# ---------------- SESSION STATE ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "active_file_hash" not in st.session_state:
    st.session_state.active_file_hash = None


# ---------------- HEADER ----------------

render_header()


# ---------------- SIDEBAR ----------------

uploaded_file, clear_chat = render_sidebar()


if clear_chat:
    st.session_state.messages = []
    st.rerun()


# ---------------- PDF PROCESSING ----------------

collection = None
document_ready = False


if uploaded_file is not None:

    pdf_bytes = uploaded_file.getvalue()

    file_hash = hashlib.sha256(
        pdf_bytes
    ).hexdigest()

    # Reset the conversation when a different PDF is uploaded.
    if st.session_state.active_file_hash != file_hash:

        st.session_state.messages = []

        st.session_state.active_file_hash = file_hash

    try:
        with st.spinner("Preparing your document..."):

            collection = get_collection(file_hash)

            # Process the PDF only if it has not been indexed.
            if collection.count() == 0:

                text = read_pdf(pdf_bytes)

                chunks = chunk_text(
                    text,
                    chunk_size=100
                )

                store_chunks(
                    collection,
                    chunks
                )

        document_ready = True

        st.success(
            f"Ready to chat with: {uploaded_file.name}"
        )

    except Exception as e:

        st.error(
            f"Could not process the PDF: {e}"
        )


# ---------------- CHAT INTERFACE ----------------

if not document_ready:

    render_empty_state()

else:

    st.markdown("### Your conversation")

    st.caption(
        "Ask questions based on the PDF you uploaded."
    )

    # Display earlier messages.
    render_chat_history(
        st.session_state.messages
    )

    question = st.chat_input(
        "Ask anything about your PDF..."
    )

    if question:

        # Save and display the user's question.
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        try:

            with st.chat_message("assistant"):

                with st.spinner(
                    "Searching your document..."
                ):

                    # Retrieve relevant PDF chunks.
                    retrieved_chunks = search_chunks(
                        collection,
                        question,
                        n_results=3
                    )

                    if not retrieved_chunks:

                        answer = (
                            "I could not find any relevant "
                            "information in the uploaded document."
                        )

                    else:

                        context = "\n\n".join(
                            retrieved_chunks
                        )

                        # Pass previous messages, excluding
                        # the current question.
                        chat_history = (
                            st.session_state.messages[:-1]
                        )

                        answer = generate_answer(
                            question,
                            context,
                            chat_history=chat_history
                        )

                st.markdown(answer)

            # Save the assistant's answer.
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        except Exception as e:

            st.error(
                f"Could not generate an answer: {e}"
            )