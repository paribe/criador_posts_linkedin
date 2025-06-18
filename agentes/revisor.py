import os
from dotenv import load_dotenv
from groq import Groq

def revisar_post(rascunho):
    """
    Revisa o post para melhorar clareza, gramática e impacto
    """
    load_dotenv()
    
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    model = os.getenv("LLM_MODEL")
    
    prompt = f"""
    Você é um revisor especializado em conteúdo profissional. Revise o post abaixo:
    
    POST ORIGINAL:
    {rascunho}
    
    MELHORIAS NECESSÁRIAS:
    - Corrigir gramática e ortografia
    - Melhorar a clareza das ideias
    - Tornar mais impactante
    - Verificar se está dentro do limite de caracteres
    - Manter o tom profissional
    - Garantir que a mensagem seja clara e objetiva
    
    Retorne apenas o post revisado, sem comentários adicionais.
    """
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro na revisão: {e}"
