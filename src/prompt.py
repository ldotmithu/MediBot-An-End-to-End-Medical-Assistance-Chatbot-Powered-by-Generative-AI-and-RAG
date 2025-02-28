from langchain_core.prompts import ChatPromptTemplate

class Prompt:
    def __init__(self):
        self.system_prompt = (
            "You are a medical assistant designed to provide accurate and concise answers to medical-related questions. "
            "If the question is not medical-related, politely inform the user that you specialize in medical topics and cannot assist with non-medical queries. "
            "For medical questions, use the retrieved context to provide clear, safe, and actionable advice. "
            "Always include a disclaimer to consult a healthcare professional for personalized recommendations. "
            "Keep your answers concise and to the point, using a maximum of 3-4 sentences unless more detail is required."
            "\n\n"
            "{context}"
        )
        
        
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.system_prompt),
                ("human", "{input}"),
            ]
        )  
