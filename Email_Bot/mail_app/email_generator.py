from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from .sentiment_analysis import calculate_polarity

def generate_llama(email_text):
    
    sentiment_score = calculate_polarity(email_text)
    
    template = """
    Analyze the content, tone, and intent of the email below and
    write an example reply, ensuring it aligns with the context,
    addresses all necessary points, and uses a tone suitable for the situation.
    Note that this example reply must be in the same language as the email.
    
    Check the sentiment score of the email: {sentiment_score} and adjust the tone accordingly.
    If the sentiment score is positive, maintain a positive and friendly tone.
    If the sentiment score is negative, be empathetic and understanding.
    Don't include the sentiment score in the reply.
    
    Please don't include your analysis in the reply. I just want the example reply.
    Email: {email}
    """
    model = OllamaLLM(model="llama3.2:1b")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    result = chain.invoke({"email": email_text, "sentiment_score": sentiment_score})
    return result