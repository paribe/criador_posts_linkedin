# Arquivo: teste_API_final.py
import os
from dotenv import load_dotenv
from groq import Groq

# Carregar variáveis de ambiente
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("LLM_MODEL")

print(f"Testando com a API Key: {api_key[:10]}...")
print(f"Modelo: {model}")

try:
    client = Groq(api_key=api_key)
    
    print("\nFazendo requisição para a API...")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "TENDENCIA DE IA EM 2025"}]
    )
    
    print("\n✅ SUCESSO! Resposta da API:")
    print("-" * 50)
    print(response.choices[0].message.content)
    print("-" * 50)
    
except Exception as e:
    print(f"❌ ERRO: {e}")
    print("\nPossíveis soluções:")
    print("1. Verificar se a API key é válida no painel do Groq")
    print("2. Verificar se há limites de rate ou créditos")
    print("3. Tentar regenerar a API key")