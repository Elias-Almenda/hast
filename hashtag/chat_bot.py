# Passo 1:
    # criar o titulo
    # criar o campo de (input)
    # mostrar quem respondeu a mensagem
    
import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key='',
                   base_url="https://generativelanguage.googleapis.com/v1beta/openai")
# titulo do chat
st.write("## ChatBot IA")

if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens'] = []
    
    
mensagem_user = st.chat_input("Diga qualquer coisa ")

for mensagens in st.session_state['lista_mensagens']:
    role = mensagens['role']
    content = mensagens['content']
    st.chat_message(role).write(content)


if mensagem_user:
    # mensagem user
    st.chat_message('user').write(mensagem_user)
    mensagem_usuario =  {'role': 'user', 'content': mensagem_user}
    st.session_state['lista_mensagens'].append(mensagem_usuario)
    
    
    # mensagem IA
    resposta_ia = modelo_ia.chat.completions.create(
        messages= st.session_state['lista_mensagens'],
        model = 'gemini-flash-lite-latest'
    )
    
    texto_resposta_ia = resposta_ia.choices[0].message.content
    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia =  {'role': 'assistant', 'content': texto_resposta_ia}
    st.session_state['lista_mensagens'].append(mensagem_ia)
