# 🩺 **Medical Chatbot - Powered by Generative AI and RAG**

## 📌 **Problem Statement**
In today's fast-paced world, access to **accurate and reliable medical information** is crucial. However, many individuals face challenges in obtaining timely medical advice due to **long wait times, lack of access to healthcare professionals, or overwhelming unreliable information online**.

This project addresses this issue by building a **Medical Chatbot** powered by **Generative AI** and **Retrieval-Augmented Generation (RAG)**. The chatbot aims to:
- **Provide instant, reliable** answers to medical-related queries.
- **Offer personalized recommendations** based on user inputs.
- **Ensure user safety** by including disclaimers and encouraging consultation with healthcare professionals.

---

## 🚀 **Project Overview**
The **Medical Chatbot** is a **Streamlit-based web application** that integrates **Groq's Mixtral-8x7b-32768 model** and **FAISS vector store** to efficiently retrieve and generate medical responses. Using a **RAG pipeline**, it ensures **context-aware and precise responses**.

### ✨ **Key Features**
- 🗨 **Conversational AI**: Engages users in real-time medical Q&A.
- 🔍 **Retrieval-Augmented Generation (RAG)**: Enhances response accuracy by fetching relevant information.
- 🎯 **Personalization**: Tailors responses based on user history and queries.
- 🔒 **Secure & Private**: Does not store personal medical data.
- 🎨 **User-Friendly Interface**: Built with **Streamlit** for seamless interaction.

---

## 🛠️ **Technologies Used**
### 📌 **AI & Machine Learning**
- **Generative AI**: [Groq's Mixtral-8x7b-32768](https://groq.com/) for response generation.
- **Vector Search**: FAISS with `sentence-transformers/all-MiniLM-L6-v2` embeddings for efficient document retrieval.
- **RAG Framework**: LangChain for integrating retrieval and generation.

### 📌 **Software & Libraries**
- **Framework**: 🖥 **Streamlit** (Web UI)
- **Programming Language**: 🐍 **Python**
- **Key Libraries**:
  - 🔗 `langchain` - For **RAG pipeline** and document handling
  - 🤖 `langchain-groq` - **Integration with Groq's LLM**
  - 📄 `PyPDFLoader` - **Loading and processing medical documents (PDFs)**
  - ⚡ `FAISS` - **Efficient similarity search**
  - 🔑 `python-dotenv` - **Managing environment variables**
  
---

### 🔧 **Steps to Run Locally**
1. **Clone the Repository**
   ```bash
   git clone https://github.com/ldotmithu/MediBot-An-End-to-End-Medical-Assistance-Chatbot-Powered-by-Generative-AI-and-RAG.git
   cd MediBot-An-End-to-End-Medical-Assistance-Chatbot-Powered-by-Generative-AI-and-RAG
   ```

2. **Create a Virtual Environment & Activate it**
   ```bash
   conda create -n medibot python=3.10 -y 
   conda activate medibot
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file in the root directory and add:
   ```env
   GROQ_API_KEY=your_groq_api_key
   ```

5. **Run the Streamlit App**
   - First, run `main.py`:
   ```bash
   python main.py 
   ```
   - Then, run Streamlit:
   ```bash
   streamlit run app.py
   ```

---

## 🔍 **How It Works**
1. 📝 **User Input**: The user types a **medical-related question** into the chatbot.
2. 🔎 **Retrieval & Augmentation**: The chatbot fetches **relevant medical information** using **FAISS** and enhances it with **Groq's LLM**.
3. 💡 **Response Generation**: The chatbot returns an **accurate, context-aware** answer in **real-time**.
4. ⚠️ **Disclaimers & Safety**: The chatbot reminds users to **consult healthcare professionals** for serious medical conditions.

---

## 🛡️ **Disclaimer**
⚠️ This chatbot is **not a substitute for professional medical advice**. It provides **general medical information and guidance**, but users should **always consult a healthcare provider** for **diagnosis and treatment**.

---

## 👥 **Contributor**
- **L. Mithurshan**

---

## 📜 **License**
📄 This project is licensed under the **Apache License**. See the [LICENSE](LICENSE) file for details.

---

### 💡 If you find this project useful, give it a ⭐ on GitHub! 🚀

