from langchain.prompts import ChatPromptTemplate
import os
from langchain_groq import ChatGroq

# Defina a chave da API
api_key = "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"
os.environ["GROQ_API_KEY"] = api_key

# Inicialize o modelo
chat = ChatGroq(model="llama-3.1-70b-versatile")


# Função para gerar a resposta do bot
def resposta_bot(mensagens):
    # Template do prompt
    prompt_template = ChatPromptTemplate.from_template(
        "Você é um assistente amigável. {mensagens}"
    )

    # Formatando as mensagens no template
    formatted_messages = prompt_template.format(
        mensagens=" ".join([f"{role}: {msg}" for role, msg in mensagens])
    )

    # Executando o chat com o modelo
    resposta = chat.invoke(formatted_messages)
    return resposta.content


# Início da interação com o usuário
print("Bem vindo")

mensagens = []
while True:
    pergunta = input("Usuário: ")
    if pergunta.lower() == "x":
        break
    mensagens.append(("user", pergunta))
    resposta = resposta_bot(mensagens)
    mensagens.append(("assistant", resposta))
    print(f"Bot: {resposta}")

print("Muito obrigado")
print(mensagens)