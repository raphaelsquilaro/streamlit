# Author: Raphael Campos Squilaro
# Project: Web Page

# Install the library with command: "pip install streamlit" in the bash

# import the libraries of streamlit
import streamlit as st

def calcular():
    return ""

# Config of page
st.set_page_config(
    page_title= "Primeria Página com streamlit",
    page_icon= "🤖",
)

# Title of page
st.title("🥔 Minha Primeira página em Python", text_alignment="center")
st.subheader("Pergunte para o Agente de IA", text_alignment="center")
st.subheader("RIA - Raphael Inteligência Artificial", text_alignment="center")

# Add a divider
st.divider(
    width= "stretch"
)

# Markdown
st.markdown("**Informe seu peso**", text_alignment="center")

# Para ter o campo de inserir o numero do pesso
st.number_input(
    label= "Digite seu peso",
    min_value= 0.0,
    max_value= 300.0,
    value= "min",
    format= "%.2f",
    placeholder= "Digite seu peso"
)

st.divider(
    width= "stretch"
)

st.markdown("**Agora, Informe sua altura (Em metros)**", text_alignment="center")

st.number_input(
    label= "Digite sua altura",
    min_value= 0.0,
    max_value= 3.0,
    value= "min",
    format= "%.2f",
    placeholder= "Digite sua altura"
)

st.button(
    "Calcular",
    on_click= "",
)

st.divider(
    width= "stretch"
)

st.text_area(
    "Resultado do IMC"
)
