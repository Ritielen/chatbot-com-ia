# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - frontend e backend
# pip install openai streamlit

import streamlit as st

from openai import OpenAI 
# modelo = OpenAI(api_key="")


st.write("# Chatbot com IA") 

# session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] =[]


# adicionar uma mensagem
# st.session_state["lista_mensagens"].append(mensagem)


texto_usuario = st.chat_input("Escreva sua mensagem aqui")

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    
    st.chat_message("user").write(texto_usuario) 
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

     # resposta da IA
     
    resposta_ia = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    
    print(resposta_ia.choices[0].message.content)

    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)


