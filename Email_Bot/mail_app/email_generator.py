from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def generate_llama(email_text):
    template = """
    Analyze the content, tone, and intent of the email below.
    Write a reply in the same language, ensuring it aligns with the context,
    addresses all necessary points, and uses a tone suitable for the situation.
    Email: {email}
    """
    model = OllamaLLM(model="llama3.2:1b")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    result = chain.invoke({"email": email_text})
    return result