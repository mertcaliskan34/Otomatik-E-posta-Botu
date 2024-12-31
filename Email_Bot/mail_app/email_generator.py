from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def generate_llama(email_text):
    template = """
    Write an answer for the email below in the language it is written.
    Email:{email}
    Answer:
    """
    model = OllamaLLM(model="llama3")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    result = chain.invoke({"email": email_text})
    return result