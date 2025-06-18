import os
from dotenv import load_dotenv
from groq import Groq

def pesquisar_tema(tema):
    """
    Pesquisa informações relevantes sobre o tema
    """
    load_dotenv()
    
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    model = os.getenv("LLM_MODEL")
    
    prompt = f"""
    Você é um pesquisador especializado. Pesquise e forneça informações relevantes sobre: {tema}
    
    Inclua:
    - Conceitos principais
    - Tendências atuais
    - Dados interessantes
    - Insights relevantes para profissionais
    - Aplicações práticas
    
    Mantenha as informações atualizadas e relevantes para 2025.
    """
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro na pesquisa: {e}"

if __name__ == "__main__":
    # Teste
    resultado = pesquisar_tema("Inteligência Artificial")
    print(resultado)
