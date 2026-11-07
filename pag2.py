import streamlit as st
import pandas as pd
from click import confirm


import Limpeza_de_dados as limpeza
from streamlit import button, slider

import Projeto_analisado
import operações

##
st.title("Tratamento de dados")##Página onde o usuário pode carregar o dataframe e manipular seus dados



if 'PA' in  st.session_state:
    PA = st.session_state['PA']

##

    if st.button(label=f'Carregar {st.session_state["nome_arquivo"]}'):
        with st.spinner(f'Carregando {st.session_state["nome_arquivo"]}'):
            st.dataframe(PA.bd)

    st.subheader("Operações no dataframe")
    st.info("Use as operações disponíveis e recarregue o dataframe para ver as mudanças!")

    operacao=st.selectbox('Tipo de operação', options=["Operação no dataframe","Operação em uma coluna específica do dataframe"])

    if operacao=="Operação no dataframe":
        st.info("""Operações que afetam/usam o dataframe inteiro:
                Contar nulos totais, Contar linhas totais""")

        opcoes=st.select_slider('Opções', options=['Contar linhas','Contar nulos'])
        if opcoes=="Contar nulos":
            st.info(f'Quantidade de valores nulos no dataset {st.session_state['nome_arquivo']}:')
            st.table(limpeza.Mostrar_Nulos(PA))

        elif opcoes=="Contar linhas":
            st.info(f'Quantidade de linhas no dataset {st.session_state['nome_arquivo']}: {limpeza.contar_linhas(PA)}')



    elif operacao=="Operação em uma coluna específica do dataframe":
        st.info("""Operações que usam os dados de uma única coluna:
            Cálculo de métricas(média,max,min,desvio padrão e etc), remoção de nulos, preenchimento de nulos
            """)

        alvo=st.selectbox('Coluna_alvo', options=PA.bd.columns)
        if PA.tipo_coluna[f'{alvo}']=="Numérica":
            opcoes = st.selectbox('Opções', options=['Escolher opção','Métricas', 'Remover Nulos', 'Preencher Nulos', 'Fazer o recorte da coluna', 'Deletar a coluna','Renomear a coluna'])
            comandos={'Escolher opção':'','Métricas':  operações.calcular, 'Remover Nulos':limpeza.Remover_Nulos, 'Preencher Nulos': limpeza.Preencher_Nulos,'Renomear a coluna': limpeza.renomear_coluna, 'Deletar a coluna': limpeza.deletar_coluna}

            if opcoes=='Preencher Nulos':
                valor=st.selectbox("Valor:", options=['Escolha um valor','0','Média','Mediana'])
                exec=comandos[opcoes](PA,alvo,valor)

            elif opcoes=='Renomear a coluna':
                nome=st.text_input("Digite o novo nome da coluna:")

                if st.button('Renomear Coluna'):
                    exec=comandos[opcoes](PA,alvo,nome)
                st.info((PA.bd[alvo].name, nome))
                st.write(PA.tipo_coluna)

            elif opcoes=='Fazer o recorte da coluna':
                st.write(f'valor mínimo atual da coluna: {PA.bd[alvo].min()}')
                limite_inferior=st.text_input('Digite o limite inferior da coluna:', placeholder='minimo')
                st.write(f'valor máximo atual da coluna: {PA.bd[alvo].max()}')
                limite_superior=st.text_input('Digite o limite superior da coluna:', placeholder='maximo')
                if limite_inferior =='':
                    limite_inferior='minimo'

                if limite_superior =='':
                    limite_superior='maximo'

                try:
                    if limite_inferior !='minimo':
                        limite_inferior=int(limite_inferior)
                    if limite_superior !='maximo':
                        limite_superior=int(limite_superior)
                except Exception as e:
                    st.error('Algum dos limites definidos é inválido, por favor use limites válidos')

                if st.button('Recortar a coluna'):
                    limpeza.recorte(PA,alvo,limite_inferior,limite_superior)

            elif opcoes == 'Escolher opção':

                pass
            else:
                exec=comandos[opcoes](PA,alvo)
        else:
            opcoes = st.selectbox('Opções',  options=['Escolher opção','Métricas', 'Remover Nulos', 'Preencher Nulos', 'Deletar a coluna','Renomear a coluna'])
            comandos={'Escolher opção':'','Métricas':  operações.calcular, 'Remover Nulos': limpeza.Remover_Nulos, 'Preencher Nulos': limpeza.Preencher_Nulos,   'Deletar a coluna':limpeza.deletar_coluna,'Renomear a coluna':limpeza.renomear_coluna}

            if opcoes == 'Preencher Nulos':
                valor = st.selectbox("Valor:", options=['Escolha um valor', '0', 'Média', 'Mediana'])
                exec = comandos[opcoes](PA, alvo, valor)


            elif opcoes == 'Renomear a coluna':

                nome = st.text_input("Digite o novo nome da coluna:")

                if st.button('Renomear Coluna'):
                    exec = comandos[opcoes](PA, alvo, nome)

                st.info((PA.bd[alvo].name, nome))

                st.write(PA.tipo_coluna)

            elif opcoes == 'Escolher opção':

                pass

            else:
                exec = comandos[opcoes](PA, alvo)

else:
    st.info("Para manipular o dataframe é preciso fazer o upload na página inicial primeiro!")