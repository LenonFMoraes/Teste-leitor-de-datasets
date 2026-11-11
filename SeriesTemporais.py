import pandas as pd
import streamlit as st
import FuncoesSeries as fs
import numpy as np
import Projeto_analisado

st.title('Series Temporais')
st.subheader('Use as funções para modelar a série')


if 'PA' in st.session_state:
    PA= st.session_state['PA']
    cols = st.columns([1, 1, 1])


    with st.container(horizontal=True ):
        x=st.selectbox(label='Coluna referente ao eixo X', options=PA.bd.columns)
        y =st.selectbox(label='Coluna referente ao eixo Y', options=PA.bd.columns)
        yplot=PA.bd[y]
    with st.container(horizontal=True):
        col = st.columns([1,1, 1])
        col[0].write('Métricas da série')
        col[0].write(PA.bd.describe())

        col[1] = fs.plot_serie(PA, x, yplot)
        col[1]= fs.acf_plot(yplot,48)
        col[1]= fs.pacf_plot(yplot,48)



    st.subheader('funções:')
    colunas=st.columns([1,1,1])

    colunas[0]= (st.text_input('Número de lags', width=100, placeholder=1))
    colunas[1]=st.button('Diferenciação')
    colunas[2]=st.button('Segunda diff')
    if colunas[1]:

            st.session_state['y2']=fs.diff(yplot,int(colunas[0]))
            col[1]=fs.plot_serie(PA, x, st.session_state['y2'])
            col[1]= fs.acf_plot(st.session_state['y2'],48)
            col[2]= fs.pacf_plot(st.session_state['y2'],48)
    if colunas[2]:
        st.session_state['y3']=fs.diff(st.session_state['y2'],int(colunas[0]))
        col[1]=fs.plot_serie(PA, x, st.session_state['y3'])
        col[1]= fs.acf_plot(st.session_state['y3'],48)
        col[2]= fs.pacf_plot(st.session_state['y3'],48)



else:
    st.warning('Carregue um dataframe para analisar a série por favor!')
