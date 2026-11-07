import os
import openpyxl
import streamlit as st
import pandas as pd
import Projeto_analisado
import Limpeza_de_dados as limpeza



st.title("Assistente de análise para dataframes")

dataset=st.file_uploader('Carregue o seu dataframe', type=Projeto_analisado.arquivos_suportados)
if dataset is not None:
    nome_arquivo=dataset.name
    st.session_state['nome_arquivo']=nome_arquivo
    _ , ext=os.path.splitext(nome_arquivo)
    leitor_automatico={"csv": pd.read_csv,"xls":pd.read_excel,'xlsx': pd.read_excel,'feather': pd.read_feather,
     "json": pd.read_json,'parquet': pd.read_parquet}

    df=leitor_automatico[f'{ext[1::]}'](dataset)

    PA=Projeto_analisado.ProjetoAnalisado(df)
    if 'PA' not in st.session_state:
        st.session_state['PA']=PA
        st.success('Projeto guardado na memória')

if 'PA' in st.session_state:
    PA=st.session_state['PA']
    st.dataframe(PA.bd)


    if st.button('Analisar Dataset'):

        with st.spinner('Analisando dataset'):
            resultados=limpeza.analisar_colunas(st.session_state['PA'])


            st.session_state['resultados']=resultados
            st.success('Dataset analisado com sucesso')
            tipo_dados=[]



            st.write(f"Seu Dataset foi analisado e possui os seguintes tipos de dados em cada coluna: \n\n ")
            st.write("Tabela usando a minha lógica de análise")
            st.table(resultados)

            st.write("Tabela usando a lógica de análise do numpy")
            st.table(PA.bd.dtypes)

            st.write(f'Colunas numéricas são compostas por valores inteiros e floats, enquanto categóricas por strings')
else:
    st.info('Faça o upload do dataframe para poder analisar os dados')