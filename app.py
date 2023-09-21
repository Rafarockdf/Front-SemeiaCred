import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.graph_objects as go
from tinydb import TinyDB
aba1,aba2=st.tabs(['Cadastro','Usuário'])
with aba1:
  st.title('Bem vindo a Semeiacred+')
  st.title('Cadastro')
  DBUser = TinyDB('user_database.json')
  print(DBUser)
  # Banco
  DBUser = TinyDB('user_database.json')
  print(DBUser)
  # Inputs
  nome=st.text_input('Digite seu nome: ')
  cnpj=st.text_input('CPF/CNPJ: ')
  idade = st.number_input('Idade:', min_value=0, step=1, format='%d', key='idade_input', value=0)
  UF = ['-','AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
  selected_uf = st.selectbox('Escolha um estado:', UF, key='uf_selectbox')
  area = st.number_input('Área (m²): ')
  categoria_prod=['-','Hortaliças', 'Agropecuária Diversa', 'Outra Categoria', 'Frutas', 'Cereais']
  selected_prod = st.selectbox('Escolha um estado:', categoria_prod, key='prod_selectbox')
  fat_medio=st.number_input('Última Média Anual de Faturamento: ')

  def inserir_dados():
    DBUser.insert({'Nome': nome,
                  'CPF/CNPJ':cnpj,
                  'Idade': idade,
                  'UF':selected_uf,
                  'Área (m²)':area,
                  'CategoriaProdutoAgricola':categoria_prod,
                  'Última Média Anual de Faturamento':fat_medio,
                  })
  if st.button('Criar o Cadatro'):
    inserir_dados()
    t=DBUser.all()
    print(t)
  

with aba2:
  
  st.title('Usuário:bust_in_silhouette:')
  st.write('Nome: ',nome)
  st.write('CNPJ: ',cnpj)
  st.write('Idade: ',idade)
  st.write('UF: ',selected_uf)
  st.write('Área (m²)',area)
  st.write('Categoria do produto: ',selected_prod)
  st.write('Última Média Anual de Faturamento:: ',fat_medio)
 
  
  x=100
  fig = go.Figure(go.Indicator(
      mode = "gauge+number",
      value =x,
      domain = {'x': [0, 1], 'y': [0, 1]},
      title = {'text': nome, 'font': {'size': 24}},
      gauge = {
          'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "black"},
          'bar': {'color': "darkblue"},
          'bgcolor': "white",
          'borderwidth': 2,
          'bordercolor': "gray",
          'steps': [
              {'range': [0, 33], 'color': 'red'},
              {'range': [34, 66], 'color': 'orange'},
              {'range': [67, 100], 'color': 'green'}],
          'threshold': {
              'line': {'color': "red", 'width': 4},
              'thickness': 0.75,
              'value': 490}}))

  fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})
  # Exibe o gráfico no Streamlit
  st.plotly_chart(fig)


