import os
from dotenv import load_dotenv
from groq import Groq

def otimizar_post(post_revisado):
    """
    Otimiza o post especificamente para o LinkedIn
    """
    load_dotenv()
    
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    model = os.getenv("LLM_MODEL")
    
    prompt = f"""
    Você é um especialista em LinkedIn. Otimize o post abaixo para máximo engajamento na plataforma:
    
    POST REVISADO:
    {post_revisado}
    
    OTIMIZAÇÕES PARA LINKEDIN:
    - Adicione emojis relevantes (mas sem exagerar)
    - Inclua hashtags estratégicas (5-10 hashtags)
    - Estruture com quebras de linha para facilitar leitura
    - Adicione call-to-action para engajamento
    - Certifique-se de que está dentro do limite de 1300 caracteres
    - Use linguagem que gere discussão
    
    Retorne apenas o post final otimizado.
    """
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro na otimização: {e}"
