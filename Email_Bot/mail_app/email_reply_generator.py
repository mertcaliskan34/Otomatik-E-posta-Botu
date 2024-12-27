from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def generate_reply(email_text):
    template = """
    Write an Answer for the email below as if you are the receiver.
    
    Email:{email}
    Answer:
    """
    model = OllamaLLM(model="llama3")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    result = chain.invoke({"email": email_text})
    return result
