import streamlit as st
import pandas as pd
import Limpeza_de_dados as limpeza
from streamlit import button, slider

import Projeto_analisado
import operações

##
st.title("Tratamento de dados")##Página onde o usuário pode carregar o dataframe e manipular seus dados


st.title("Assistente de análise para dataframes")
st.write("Bem-vindo! Esta ferramenta foi feita para ajudar a entender datasets.")
if 'PA' in  st.session_state:
    PA = st.session_state['PA']

##

    if st.button(label='Carregar Dataframe', ):
        with st.spinner('Carregando Dataframe...'):
            st.dataframe(PA.bd)

    st.subheader("Operações no dataframe")
    st.info("Use as operações disponíveis e recarregue o dataframe para ver as mudanças!")

    operacao=st.selectbox('Tipo de operação', options=["Operação no dataframe","Operação em uma coluna específica do dataframe"])

    if operacao=="Operação no dataframe":
        st.info("""Operações que afetam/usam o dataframe inteiro:
                Contar nulos totais, Contar linhas totais""")

        opcoes=st.select_slider('Opções', options=['Contar linhas','Contar nulos','Remover nulos'])
        if opcoes=="Contar nulos":
            st.info(f'Quantidade de valores nulos:{limpeza.Mostrar_Nulos(PA)} ')
        elif opcoes=="Contar linhas":
            st.info(f'Quantidade de linhas:{limpeza.contar_linhas(PA)}')



    elif operacao=="Operação em uma coluna específica do dataframe":
        st.info("""Operações que usam os dados de uma única coluna:
            Cálculo de métricas(média,max,min,desvio padrão e etc), remoção de nulos, preenchimento de nulos e
            teste de distribuições(fit)
            """)

        alvo=st.selectbox('Coluna_alvo', options=PA.bd.columns)
        if PA.tipo_coluna[f'{alvo}']=="Numérica":
            opcoes = st.selectbox('Opções', options=['Métricas', 'teste de distribuições', 'Remover Nulos', 'Preencher Nulos', 'Fazer o recorte da coluna', 'Deletar a coluna'])
            comandos={'Métricas':  operações.calcular, 'Remover Nulos':limpeza.Remover_Nulos, 'Preencher Nulos': limpeza.Preencher_Nulos }

            if opcoes=='Preencher Nulos':
                valor=st.selectbox("Valor:", options=['Escolha um valor','0','Média','Mediana'])
                exec=comandos[opcoes](PA,alvo,valor)

            else:
                exec=comandos[opcoes](PA,alvo)
        else:
            opcoes = st.selectbox('Opções',  options=['Métricas', 'Remover Nulos', 'Preencher Nulos',  'teste de distribuições', 'Fazer o recorte da coluna', 'Deletar a coluna'])
            comandos={'Métricas':  operações.calcular, 'Remover Nulos': limpeza.Remover_Nulos, 'Preencher Nulos': limpeza.Preencher_Nulos,  'teste de distribuições': 'a' , 'Fazer o recorte da coluna':'', 'Deletar a coluna':''}

            if opcoes == 'Preencher Nulos':
                valor = st.selectbox("Valor:", options=['Escolha um valor', '0', 'Média', 'Mediana'])
                exec = comandos[opcoes](PA, alvo, valor)

            else:
                exec = comandos[opcoes](PA, alvo)
else:
    st.info("Para manipular o dataframe é preciso fazer o upload na página inicial primeiro!")