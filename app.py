import streamlit as st
from src.prompt import Prompt
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from src.store_index import GetIndex


load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")


index_path = "faiss_index"
prompt = Prompt()
vector_db = GetIndex(index_path)

vecter_store = vector_db.get_index()


llm = ChatGroq(api_key=GROQ_API_KEY, model_name="mixtral-8x7b-32768",temperature=0.5)


question_answer_chain = create_stuff_documents_chain(llm, prompt.prompt)
rag_chain = create_retrieval_chain(vecter_store.as_retriever(), question_answer_chain)


def main():
    st.set_page_config(
        page_title="Medical Chatbot",
        page_icon="🩺",
        layout="centered",
    )



    st.title("🩺 Medical Chatbot")
    st.markdown("Welcome to the Medical Chatbot! Ask any medical-related questions, and I'll do my best to provide accurate and concise answers.")


    if "messages" not in st.session_state:
        st.session_state.messages = []

    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

  
    user_input = st.chat_input("Ask a medical question...")

    if user_input:
        
        st.session_state.messages.append({"role": "user", "content": user_input})

        
        with st.chat_message("user"):
            st.markdown(user_input)


        with st.spinner("Thinking..."):
            response = rag_chain.invoke({"input": user_input})
            bot_response = response["answer"]

       
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

      
        with st.chat_message("assistant"):
            st.markdown(bot_response)


if __name__ == "__main__":
    main()