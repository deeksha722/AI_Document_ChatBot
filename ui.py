
import streamlit as st


def apply_design():
    st.set_page_config(
        page_title="DocuChat AI",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown(
        """
        <style>
        .stApp {
            background: #f8f9fd;
            color: #172033;
        }

        .block-container {
            max-width: 1050px;
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }

        section[data-testid="stSidebar"] {
            background: #ffffff;
            border-right: 1px solid #e8eaf2;
        }

        .hero {
            background: linear-gradient(120deg, #202c66, #5546d7);
            padding: 28px 30px;
            border-radius: 20px;
            margin-bottom: 24px;
            color: white;
        }

        .hero h1 {
            color: white !important;
        }

        .hero p {
            color: #e5e7ff !important;
            line-height: 1.6;
        }

        [data-testid="stChatMessage"] {
            background: white;
            border: 1px solid #e8eaf2;
            border-radius: 17px;
            padding: 16px;
            margin-bottom: 14px;
        }

        .stButton > button {
            border-radius: 11px;
            font-weight: 600;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def render_header():
    st.markdown(
        """
        <div class="hero">
            <h1>📚 DocuChat AI</h1>
            <p>
                Your personal AI document assistant.
                Upload a PDF and explore your knowledge.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_sidebar():
    with st.sidebar:
        st.markdown("## 📚 DocuChat AI")
        st.caption("Your knowledge, one conversation away.")
        st.markdown("---")
        st.markdown("### 📄 Your document")

        uploaded_file = st.file_uploader(
            "Upload a PDF to begin",
            type=["pdf"]
        )

        if uploaded_file is not None:
            st.success("PDF selected")
            st.caption(f"File: {uploaded_file.name}")

        st.markdown("---")
        st.markdown("### ✨ How it works")
        st.caption("1. Upload your PDF")
        st.caption("2. Ask questions")
        st.caption("3. Get document-based answers")

        st.markdown("---")

        clear_chat = st.button(
            "🗑️ Clear conversation",
            use_container_width=True
        )

    return uploaded_file, clear_chat


def render_empty_state():
    st.markdown("### Welcome to your workspace 👋")
    st.write("Upload a PDF to start chatting with your document.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 📖 Understand")
        st.caption("Get simple explanations of difficult topics.")

    with col2:
        st.markdown("#### 🔎 Find answers")
        st.caption("Search for information in your document.")

    with col3:
        st.markdown("#### 📝 Summarize")
        st.caption("Get concise summaries of important topics.")


def render_chat_history(messages):
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def render_footer():
    st.markdown("---")
    st.caption(
        "DocuChat AI · Ask questions. Discover insights."
    )
